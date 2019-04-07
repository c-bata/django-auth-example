from django.test import TestCase
from snippets.models import Snippet
from snippets.forms import SnippetForm


class SnippetFormTests(TestCase):
    def test_valid(self):
        params = {
            'title': 'hello world',
            'code': 'print("Hello World")',
            'description': 'Just printing "Hello World"',
        }
        snippet = Snippet()
        form = SnippetForm(params, instance=snippet)
        self.assertTrue(form.is_valid())

    def test_should_specify_title(self):
        params = {}
        snippet = Snippet()
        form = SnippetForm(params, instance=snippet)
        self.assertFalse(form.is_valid())
