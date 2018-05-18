from django.conf import settings
from django.db import models


class Social(models.Model):
    """Social Auth association model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='socials',
                             on_delete=models.CASCADE)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)

    class Meta:
        unique_together = ('provider', 'uid')
        db_table = 'socials'
