from django.test import TestCase, Client


class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        c = Client()
        response = c.get("/")
        self.assertTemplateUsed(response, "top.html")
