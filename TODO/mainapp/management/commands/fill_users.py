import json
import os
import random
import uuid

from django.contrib.auth.models import User
from mimesis.locales import Locale

from mainapp.models import BaseUser
from django.core.management.base import BaseCommand

from tasks.models import Project, Todo
import mimesis

JSON_PATH = 'mainapp/jsons'
NUMBER_OF_STRINGS = 1000

class Command(BaseCommand):
    def handle(self, *args, **options):
        BaseUser.objects.all().delete()
        persona = mimesis.Person('ru')
        for _ in range(NUMBER_OF_STRINGS):
            new_user = BaseUser(
                username=persona.username(),
                firstname=persona.first_name(),
                lastname=persona.last_name(),
                email=persona.email(),
                password=persona.password(),
                is_staff=random.choice([True, False]),
                created_at=mimesis.Datetime(Locale.RU).datetime(start=2010)
            )

            new_user.save()

        Project.objects.all().delete()
        texts = mimesis.Text()
        internet_obj = mimesis.Internet()
        uuids = BaseUser.objects.values("uuid")
        for _ in range(NUMBER_OF_STRINGS):
            uuid_project = random.choice(uuids)
            # print(uuid_project)
            # print(BaseUser.objects.filter(uuid=uuid_project['uuid']).first())
            new_project = Project(
                name=texts.word(),
                repohref=internet_obj.url(),
                user=BaseUser.objects.filter(uuid=uuid_project['uuid']).first(),
                created_at=mimesis.Datetime(Locale.RU).datetime(start=2010)
            )
            new_project.save()

        Todo.objects.all().delete()
        uuids_projects = Project.objects.values("uuid")

        for _ in range(NUMBER_OF_STRINGS):
            uuid_theme = random.choice(uuids_projects)
            author_uuid = random.choice(uuids)
            new_todo = Todo(
                project=Project.objects.filter(uuid=uuid_theme['uuid']).first(),
                text=texts.text(quantity=2),
                author=BaseUser.objects.filter(uuid=author_uuid['uuid']).first(),
                created_at=mimesis.Datetime(Locale.RU).datetime(start=2010)
            )
            new_todo.save()


        super_user = User.objects.create_superuser('admin', 'admin@mail.local', 'qwerty')
        if super_user:
            print('All done')
