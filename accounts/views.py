import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from socials.models import Social
from .forms import UserCreationForm

logger = logging.getLogger('auth_example.accounts')


def signup(request):
    social_uid = request.session.get('social_uid')
    social_provider = request.session.get('social_provider')

    if social_uid == "" or social_provider == "":
        return HttpResponseBadRequest("Please retry Github authentication".encode('utf-8'))

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            if social_uid != "" and social_provider != "":
                social = Social.objects.get(provider=social_provider, uid=social_uid)
                social.user = user
                social.save()

            messages.add_message(request, messages.SUCCESS, f"Success to register account.")
            login(request, user, "django.contrib.auth.backends.ModelBackend")  # redirect to LOGIN_REDIRECT_URL
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserCreationForm(initial={
            "username": request.session.get('social_username'),
            "email": request.session.get('social_email'),
        })
    return render(request, 'accounts/signup.html', {'form': form})
