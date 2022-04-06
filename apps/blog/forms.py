from django import forms
from .models import Comment, VideoComment
from apps.users.models import Email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ("email",)
