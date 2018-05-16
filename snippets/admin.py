from django.contrib import admin

from snippets.models import Snippet, Comment

admin.site.register(Snippet)
admin.site.register(Comment)
