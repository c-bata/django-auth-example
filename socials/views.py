from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from socials import github
from socials.models import Social

BACKENDS = settings.AUTHENTICATION_BACKENDS


@never_cache
def auth(request, provider):
    pass


@never_cache
def complete(request, provider):
    if provider == "github":
        code = request.GET['code']
        payload = {
            "client_id": settings.SOCIAL_AUTH_GITHUB_KEY,
            "client_secret": settings.SOCIAL_AUTH_GITHUB_SECRET,
            "code": code,
        }
        access_token = github.get_access_token(payload)
        user_info = github.get_github_user_info(access_token)
        user = github.get_or_create_user(
            nickname=user_info['login'],
            provider='github',
            uid=user_info['id'],
            email=user_info['email'],
        )
        login(request, user)
    else:
        raise Http404('Unsupported provider')
    return HttpResponseRedirect("/")


@never_cache
def disconnect(request, provider):
    try:
        Social.objects.get(user_id=request.user.id, provider=provider).delete()
    except Social.ObjectDoesNotExist:
        raise Http404('Unsupported provider')
    return HttpResponseRedirect("/")
