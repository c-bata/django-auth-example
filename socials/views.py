import logging

from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from . import github
from .models import Social

logger = logging.getLogger('slidepress.social')


@never_cache
def complete(request, provider):
    social = None
    uid = None
    username = None
    email = None
    if provider == "github":
        access_token = github.get_access_token(request)
        user_info = github.get_github_user_info(access_token)

        uid = user_info.get('id')
        email = user_info.get('email')
        username = user_info.get('login')
        if not uid:
            return HttpResponseBadRequest('"id" fields must not be empty'.encode('utf-8'))
    else:
        raise Http404('Unsupported provider')

    social, created = Social.objects.get_or_create(provider=provider, uid=uid)
    if created:
        logger.info(f"new social account registered: {uid} {provider} {username} {email}")

    if social.user_id is None:
        request.session['social_uid'] = uid
        request.session['social_provider'] = provider
        request.session['social_username'] = username
        request.session['social_email'] = email
        return redirect(reverse('signup'))

    user = get_user_model().objects.get(id=social.user_id)
    login(request, user, 'django.contrib.auth.backends.ModelBackend')
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


@never_cache
def disconnect(request, provider):
    try:
        Social.objects.get(user_id=request.user.id, provider=provider).delete()
    except Social.ObjectDoesNotExist:
        raise Http404('Unsupported provider')
    return HttpResponseRedirect("/")
