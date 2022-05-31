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

        # todos = load_from_json('todo')
        #
        # Todo.objects.all().delete()
        # for todo in todos:
        #     todo_author = uuid.UUID(todo['author'])
        #     todo_project = uuid.UUID(todo['project_id'])
        #     print(f'________________________{todo_project}_______________________________')
        #     _uuid = BaseUser.objects.get(uuid=todo_author)
        #     print(f'________________________{repr(_uuid)}_______________________________')
        #
        #     _project = Project.objects.get(uuid=todo_project)
        #     print(f'________________________{repr(_project)}_______________________________')
        #
        #     todo['author'] = _uuid
        #     todo['project_id'] = _project
        #     new_todo = Todo(**todo)
        #     new_todo.save()

        super_user = User.objects.create_superuser('admin', 'admin@mail.local', 'qwerty')
        if super_user:
            print('All done')
