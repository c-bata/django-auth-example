import logging

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from socials.models import Social

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

        messages.add_message(self.request, messages.SUCCESS,
                             "ユーザー登録に成功しました。")
        login(self.request, user,
              "django.contrib.auth.backends.ModelBackend")
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "ユーザー登録に失敗しました。")
        return super().form_invalid(form)
