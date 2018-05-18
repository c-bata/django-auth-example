from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from .. import views


class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEquals(view.func, views.signup)


class LoginPageTest(TestCase):
    def test_top_page_returns_200(self):
        c = Client()
        response = c.get("/accounts/login/")
        self.assertEqual(200, response.status_code)


class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_view_function(self):
        view = resolve('/accounts/password_reset/done/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetDoneView)

