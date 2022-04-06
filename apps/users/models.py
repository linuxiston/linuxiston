from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Email(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "email"
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email
