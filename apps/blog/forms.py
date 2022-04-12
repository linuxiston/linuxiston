from django import forms
from .models import Comment, VideoComment, Contact, Post
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


class WritePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'tags', 'title', 'description', 'body', 'thumbnail')

    category = forms.Select()
