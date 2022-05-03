import json
import os

from django.contrib.auth.models import User

from mainapp.models import BaseUser
from django.core.management.base import BaseCommand

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')

        BaseUser.objects.all().delete()
        super_user = User.objects.create_superuser('admin', 'admin@mail.local', 'qwerty')
        for user in users:
            new_user = BaseUser(**user)
            new_user.save()
        if super_user:
            print('All done')