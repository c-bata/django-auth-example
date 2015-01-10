from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'accounts/logged_out.html'}),
)