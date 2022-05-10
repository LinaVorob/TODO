from django.utils.timezone import now

from mainapp.models import BaseUser

from django.db import models
from uuid import uuid4


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    repohref = models.URLField(null=True)
    user = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Todo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    users = models.ManyToManyField(BaseUser)
    author = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())
    status = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.project}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'