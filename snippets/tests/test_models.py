from django.contrib.auth import get_user_model
from django.test import TestCase
from snippets.models import Snippet

UserModel = get_user_model()


class SnippetManagerTests(TestCase):
    def test_public_snippet_manager(self):
        user = UserModel.objects.create_user(username='c-bata', email='shibata@example.com', password='secret')
        Snippet.objects.create(title="title1", created_by=user, is_draft=False)
        Snippet.objects.create(title="title2", created_by=user, is_draft=True)
        Snippet.objects.create(title="title3", created_by=user, is_draft=False)

        snippets = Snippet.public_objects.all()
        self.assertEqual(len(snippets), 2)


class SnippetModelTests(TestCase):
    def test_short_description_with_long_text(self):
        snippet = Snippet(title="title", description="あいうえおかきくけこさしすせそ")
        self.assertEqual(snippet.short_description, "あいうえおかきくけこ")

    def test_short_description_with_short_text(self):
        snippet = Snippet(title="title", description="あいうえお")
        self.assertEqual(snippet.short_description, "あいうえお")
