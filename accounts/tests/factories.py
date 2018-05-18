import factory
import pytz
from django.conf import settings
from django.utils import timezone
from factory import fuzzy
import string

from django.contrib.auth import get_user_model

UserModel = get_user_model()
FAKER_LOCALE = 'ja_JP'
tzinfo = pytz.timezone(settings.TIME_ZONE)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = fuzzy.FuzzyText(length=5, chars=string.ascii_lowercase + "0123456789-")
    email = factory.Faker("email", FAKER_LOCALE)
    display_name = factory.Faker("name", FAKER_LOCALE)
    is_admin = False
    is_staff = False
    is_active = True
    date_joined = fuzzy.FuzzyDateTime(timezone.datetime(2016, 1, 1, tzinfo=tzinfo),
                                      timezone.datetime(2018, 8, 1, tzinfo=tzinfo))
