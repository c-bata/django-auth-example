from django.db import models
from user_auth import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks')
    summary = models.CharField('タスク', max_length=128)
    complete = models.BooleanField('状態', default=False)
    comment = models.CharField('コメント', max_length=512, blank=True)
    done_date = models.DateField('完了日', null=True, blank=True)

    def __str__(self):
        return str(self.id) + ': ' + self.summary
