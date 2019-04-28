from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS,
                             "ユーザー登録に成功しました。")
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "ユーザー登録に失敗しました。")
        return super().form_invalid(form)
