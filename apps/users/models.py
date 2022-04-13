from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="author-avatars", null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    telegram = models.URLField(null=True, blank=True, default='#')
    instagram = models.URLField(null=True, blank=True, default='#')
    youtube = models.URLField(null=True, blank=True, default='#')
    github = models.URLField(null=True, blank=True, default='#')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def image(self):
        if self.avatar:
            return self.avatar.url
        else:
            if self.socialaccount_set.filter(provider='google'):
                url = self.socialaccount_set.filter(provider='google')[0].extra_data['picture']
            else:
                url = self.socialaccount_set.filter(provider='github')[0].extra_data['avatar_url']
            return url


class Email(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "email"
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email
