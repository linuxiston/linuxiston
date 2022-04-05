from django import forms
from .models import Comment, VideoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
