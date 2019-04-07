from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

UserModel = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserModel
        fields = 'username',
