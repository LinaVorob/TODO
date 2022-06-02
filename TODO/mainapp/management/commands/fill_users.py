import json
import os
import uuid

from django.contrib.auth.models import User

from mainapp.models import BaseUser
from django.core.management.base import BaseCommand

from tasks.models import Project, Todo

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')

        BaseUser.objects.all().delete()
        for user in users:
            new_user = BaseUser(**user)
            new_user.save()

        projects = load_from_json('projects')

        Project.objects.all().delete()
        for project in projects:
            project_uuid = uuid.UUID(project['user'])
            _uuid = BaseUser.objects.get(uuid=project_uuid)
            project['user'] = _uuid
            new_project = Project(**project)
            new_project.save()

        super_user = User.objects.create_superuser('admin', 'admin@mail.local', 'qwerty')
        if super_user:
            print('All done')
