from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)
