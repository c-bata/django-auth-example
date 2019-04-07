FROM python:3.7
MAINTAINER Masashi Shibata <contact@c-bata.link>

RUN apt-get update && apt-get install -y --no-install-recommends git gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ADD . /usr/src
RUN pip install -r /usr/src/requirements.txt

WORKDIR /usr/src
EXPOSE 80
CMD ["gunicorn", "-w", "4", "-b", ":80", "djangosnippets.wsgi:application"]
