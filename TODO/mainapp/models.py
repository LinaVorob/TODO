from django.db import models
from uuid import uuid4


class BaseUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64, null=True)
    lastname = models.CharField(max_length=64, null=True)
    email = models.EmailField(unique=True)
    password = models.TextField()

    def __str__(self):
        return f'{self.username} /// {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'