from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image_url = models.URLField('画像URL', blank=True)
