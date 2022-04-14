from django import forms
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class UserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'bio', 'telegram', 'instagram', 'youtube', 'github')
