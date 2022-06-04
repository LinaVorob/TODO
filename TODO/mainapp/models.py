from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

from django.db.models import Model
from django.utils.timezone import now


class BaseUser(Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64, null=True)
    lastname = models.CharField(max_length=64, null=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    is_superuser = models.BooleanField(null=False, default=False)
    is_staff = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.username} /// {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'