from django import forms
from .models import Comment, VideoComment, Contact
from apps.users.models import Email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class CommentVideForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ("comment",)


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ("email",)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
