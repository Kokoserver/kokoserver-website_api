from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User as UserModel

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = [
            'email', 'tagname'
        ]

class ChangeUserForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = [
            'email', 'tagname'
        ]