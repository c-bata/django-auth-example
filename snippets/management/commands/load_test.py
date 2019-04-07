from concurrent.futures.thread import ThreadPoolExecutor
from django.core.management.base import BaseCommand
import requests
from requests.auth import HTTPBasicAuth
import time
from threading import Lock
from typing import Iterator, Tuple


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate  # per second
        self.tokens = 0.0
        self.last = 0

    def consume(self, amount=1):
        if amount > self.rate:
            raise ValueError("amount must be less or equal to rate")

        with self._consume_lock:
            while True:
                now = time.time()

                if self.last == 0:
                    self.last = now

                elapsed = now - self.last
                self.tokens += elapsed * self.rate
                self.last = now

                if self.tokens > self.rate:
                    self.tokens = self.rate

                if self.tokens >= amount:
                    self.tokens -= amount
                    return amount

                time.sleep((amount - self.tokens) / self.rate)


def fetch_with_throttle(url: str, throttle: Throttle,
                        username: str = None, password: str = None) -> (int, bool):
    # returned values: status_code, timeout
    throttle.consume()

    try:
        if username:
            res = requests.get(url, timeout=5, auth=HTTPBasicAuth(username, password))
        else:
            res = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return 0, True
    except requests.exceptions.ConnectionError:
        # Sometimes this exception was happened with following message:
        # ('Connection aborted.', BrokenPipeError(32, 'Broken pipe'))
        return fetch_with_throttle(throttle)
    return res.status_code, False


def fetch(url: str, username: str = None, password: str = None) -> (int, bool):
    # returns: status_code, timeout
    try:
        if username:
            res = requests.get(url, timeout=5, auth=HTTPBasicAuth(username, password))
        else:
            res = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return 0, True
    except requests.exceptions.ConnectionError:
        # Sometimes this exception was happened with following message:
        # ('Connection aborted.', BrokenPipeError(32, 'Broken pipe'))
        return fetch()
    return res.status_code, False


def print_result(results: Iterator[Tuple[int, str]], elapsed: float):
    cnt_req, cnt2xx, cnt4xx, cnt5xx, cnt_timeout = 0, 0, 0, 0, 0

    for r in results:
        status_code = r[0]
        timeout = r[1]
        cnt_req += 1
        if timeout:
            cnt_timeout += 1
        elif 200 <= status_code < 300:
            cnt2xx += 1
        elif 400 <= status_code < 500:
            cnt4xx += 1
        elif 500 <= status_code:
            cnt5xx += 1

    print(f"{elapsed:.3f} secs / {cnt_req} req, "
          f"2xx={cnt2xx} 4xx={cnt4xx} 5xx={cnt5xx} timeout={cnt_timeout}")


class Command(BaseCommand):
    help = 'Insert dummy users and dummy snippets'

    def add_arguments(self, parser):
        parser.add_argument('--login', action='store_true',
                            help='send requests from authenticated user')
        parser.add_argument('--throttle', type=int, default=0,
                            help='Throttling rate. Not throttling if given 0')
        parser.add_argument('--username', help='Login username')
        parser.add_argument('--password', help='Login password')
        parser.add_argument('--url', help='Request url',
                            default='http://127.0.0.1:8000/api/snippets/')

    def handle(self, *args, **options):
        throttle_rate: int = options.get('throttle')
        username: str = options.get('username')
        password: str = options.get('password')
        url: str = options.get('url')

        throttle: Throttle = None
        if throttle_rate > 0:
            throttle = Throttle(throttle_rate)

        while True:
            start = time.time()
            with ThreadPoolExecutor(10) as pool:
                if throttle_rate > 0:
                    results = pool.map(lambda a: fetch_with_throttle(*a),
                                       [(url, throttle, username, password) for _ in range(20)])
                else:
                    results = pool.map(lambda a: fetch(*a),
                                       [(url, username, password) for _ in range(20)])
            end = time.time()
            elapsed = end - start
            print_result(results, elapsed)
