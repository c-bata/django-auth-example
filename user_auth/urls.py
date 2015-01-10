from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'web.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'accounts/logged_out.html'}),
)
