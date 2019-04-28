import logging

from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect

from socials.models import Social
from .forms import UserCreationForm, UserChangeForm

logger = logging.getLogger('auth_example.accounts')


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('top')

    def get_initial(self):
        return {
            "username": self.request.session.get('social_username'),
            "email": self.request.session.get('social_email'),
        }

    def form_valid(self, form):
        user = form.save()
        social_uid = self.request.session.get('social_uid')
        social_provider = self.request.session.get('social_provider')
        if social_uid and social_provider:
            social = Social.objects.get(provider=social_provider, uid=social_uid)
            social.user = user
            social.save()

        self.object = user
        messages.add_message(self.request, messages.SUCCESS,
                             f"Success to register account.")
        login(self.request, user,
              "django.contrib.auth.backends.ModelBackend")
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Failed to sign up")
        return super().form_invalid(form)


class UserChangeView(UpdateView):
    form_class = UserChangeForm
    template_name = "accounts/change.html"
    success_url = reverse_lazy('change')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             f"Failed to change user info")
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user
