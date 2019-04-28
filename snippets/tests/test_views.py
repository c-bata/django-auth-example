import pytz
from unittest import mock

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.test import TestCase, RequestFactory
from django.utils import timezone

from snippets.tests.factories import SnippetFactory
from snippets.views import new_snippet, list_recently_updated_snippets

UserModel = get_user_model()


tzinfo = pytz.timezone(settings.TIME_ZONE)
current_datetime = timezone.datetime(year=2019, month=1, day=15, hour=12, tzinfo=tzinfo)


class ListRecentlyUpdatedSnippetsTests(TestCase):
    @mock.patch('django.utils.timezone.now', return_value=current_datetime)
    def test_should_match_only_updated_two_days_ago(self, mock_now):
        SnippetFactory(updated_at=current_datetime - timezone.timedelta(days=2))
        SnippetFactory(updated_at=current_datetime - timezone.timedelta(days=4))
        actual = list_recently_updated_snippets(days=3)
        expected_snippet_counts = 2
        self.assertEqual(len(actual), expected_snippet_counts)
        self.assertTrue(mock_now.called)


class SnippetCreateViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='c-bata', email='shibata@example.com', password='secret')

    def test_should_return_200_if_sending_get_request(self):
        request = self.factory.get("/endpoint/of/create_snippet")
        request.user = self.user
        response = new_snippet(request)
        self.assertEqual(response.status_code, 200)

    def test_should_redirect_if_user_does_not_login(self):
        request = self.factory.get("/endpoint/of/create_snippet")
        request.user = AnonymousUser()
        response = new_snippet(request)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_should_return_400_if_sending_empty_post_request(self):
        request = self.factory.post("/endpoint/of/create_snippet", data={})
        request.user = self.user
        response = new_snippet(request)
        self.assertEqual(response.status_code, 400)

    def test_should_return_201_if_sending_valid_post_request(self):
        request = self.factory.post("/endpoint/of/create_snippet", data={
            'title': 'hello world',
            'code': 'print("Hello World")',
            'description': 'Just printing "Hello World"',
        })
        request.user = self.user
        response = new_snippet(request)
        self.assertIsInstance(response, HttpResponseRedirect)
