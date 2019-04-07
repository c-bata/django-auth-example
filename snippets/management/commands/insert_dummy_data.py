import random

from django.core.management.base import BaseCommand
from accounts.tests.factories import UserFactory
from snippets.tests.factories import SnippetFactory


class Command(BaseCommand):
    help = 'Insert dummy users and dummy snippets'

    def add_arguments(self, parser):
        parser.add_argument('account_count', nargs='?', type=int)
        parser.add_argument('snippet_count', nargs='?', type=int)

    def handle(self, *args, **options):
        account_count = options.get("account_count")
        snippet_count = options.get("snippet_count")
        if not account_count:
            account_count = 100
        if not snippet_count:
            snippet_count = 1000

        users = []
        for i in range(account_count):
            users.append(UserFactory())

        for i in range(snippet_count):
            user = random.choice(users)
            SnippetFactory(created_by=user)
