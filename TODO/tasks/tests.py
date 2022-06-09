from uuid import UUID

from django.test import TestCase
import json

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APISimpleTestCase, force_authenticate, APIClient
from django.contrib.auth.models import User
# from .views import ProjectViewSet
# from .models import Project
from mainapp.views import UserViewSet
from mainapp.models import BaseUser
from tasks.models import Project


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/userss')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_test(self):
        factory = APIRequestFactory()
        request = factory.post('/users', {
            'username': 'Sarah96',
            'firstname': 'Sarah',
            "lastname": 'Smith',
            'email': 'sarahsmith96@yandex.ru',
            'password': 'sarahspassword'
        })
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/users', {
            'username': 'Sarah96',
            'firstname': 'Sarah',
            "lastname": 'Smith',
            'email': 'sarahsmith96@yandex.ru',
            'password': 'sarahspassword'
        })
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = BaseUser.objects.create(
            username='Sarah96',
            firstname='Sarah',
            lastname='Smith',
            email='sarahsmith96@yandex.ru',
            password='sarahspassword')
        client = APIClient()
        response = client.get(f'/users/{user.uuid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = BaseUser.objects.create(
            username='Sarah96',
            firstname='Sarah',
            lastname='Smith',
            email='sarahsmith96@yandex.ru',
            password='sarahspassword')
        client = APIClient()
        response = client.put(f'/users/{user.uuid}/', {
            'username': 'Tim2000',
            'firstname': 'Timmy',
            "lastname": 'Brown',
            'email': 'timover2000@yandex.ru',
            'password': 'timybrown'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = BaseUser.objects.create(
            username='Sarah96',
            firstname='Sarah',
            lastname='Smith',
            email='sarahsmith96@yandex.ru',
            password='sarahspassword')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
        client.login(username='admin', password='qwerty')
        response = client.put(f'/users/{user.uuid}/', {
            'username': 'Tim2000',
            'firstname': 'Timmy',
            "lastname": 'Brown',
            'email': 'timover2000@yandex.ru',
        })
        user = BaseUser.objects.get(uuid=user.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.username, 'Tim2000')
        self.assertEqual(user.firstname, 'Timmy')
        self.assertEqual(user.lastname, 'Brown')
        self.assertEqual(user.email, 'timover2000@yandex.ru')
        client.logout()


class TestProjectViewSet(APITestCase):
    def test_projects_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_project_admin(self):
        project = mixer.blend(Project)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
        self.client.login(username='admin', password='qwerty')
        response = self.client.put(f'/projects/{project.uuid}/', {
            'name': 'Hermitage',
            'repohref': 'http://hermitage.ru',
            'user': project.user.uuid
        })
        print(response.json())
        project = Project.objects.get(uuid=project.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(project.name, 'Hermitage')
        self.client.logout()

