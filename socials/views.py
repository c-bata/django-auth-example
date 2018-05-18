from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.http import Http404
from django.urls import reverse
from django.views.decorators.cache import never_cache
from social_core.actions import do_auth, do_complete, do_disconnect
from social_core.backends.utils import get_backend
from social_core.exceptions import MissingBackend
from social_django.strategy import DjangoStrategy
from social_django.models import DjangoStorage
from social_django.views import _do_login as login_func

BACKENDS = settings.AUTHENTICATION_BACKENDS


@never_cache
def auth(request, provider):
    redirect_uri = reverse("social:complete", args=(provider,))
    request.social_strategy = DjangoStrategy(DjangoStorage, request)
    try:
        backend_cls = get_backend(BACKENDS, provider)
        backend_obj = backend_cls(request.social_strategy, redirect_uri)
    except MissingBackend:
        raise Http404('Backend not found')

    return do_auth(backend_obj, redirect_name=REDIRECT_FIELD_NAME)


@never_cache
def complete(request, provider):
    redirect_uri = reverse("social:complete", args=(provider,))
    request.social_strategy = DjangoStrategy(DjangoStorage, request)
    try:
        backend_cls = get_backend(BACKENDS, provider)
        backend_obj = backend_cls(request.social_strategy, redirect_uri)
    except MissingBackend:
        raise Http404('Backend not found')

    return do_complete(backend_obj, login_func, request.user,
                       redirect_name=REDIRECT_FIELD_NAME, request=request)


@never_cache
def disconnect(request, provider, association_id=None):
    request.social_strategy = DjangoStrategy(DjangoStorage, request)
    try:
        backend_cls = get_backend(BACKENDS, provider)
        backend_obj = backend_cls(request.social_strategy, "")
    except MissingBackend:
        raise Http404('Backend not found')

    return do_disconnect(backend_obj, request.user, association_id,
                         redirect_name=REDIRECT_FIELD_NAME)
