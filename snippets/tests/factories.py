from datetime import timedelta
import factory
import pytz
from random import randint

from django.conf import settings
from django.utils import timezone
from factory import fuzzy

from accounts.tests.factories import UserFactory
from snippets.models import Snippet, Comment

tzinfo = pytz.timezone(settings.TIME_ZONE)


class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet

    title = fuzzy.FuzzyText(prefix='title_', length=16)
    code = fuzzy.FuzzyText(prefix='code_')
    is_draft = fuzzy.FuzzyChoice(choices=[True, False])
    created_by = factory.SubFactory(UserFactory)
    description = fuzzy.FuzzyText(prefix='description_', length=64)
    created_at = fuzzy.FuzzyDateTime(timezone.datetime(2016, 1, 1, tzinfo=tzinfo),
                                     timezone.datetime(2018, 8, 1, tzinfo=tzinfo))
    updated_at = factory.LazyAttribute(lambda o: o.created_at + timedelta(randint(1, 28)))


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = fuzzy.FuzzyText(prefix='comment_', length=16)
    commented_at = fuzzy.FuzzyDateTime(timezone.datetime(2016, 1, 1, tzinfo=tzinfo),
                                       timezone.datetime(2018, 8, 1, tzinfo=tzinfo))
    commented_to = factory.SubFactory(SnippetFactory)
    commented_by = factory.SubFactory(UserFactory)
