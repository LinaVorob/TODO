from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from TODO.serializers import ProjectModelSerializer, ToDoModelSerializer
from tasks.models import Project, Todo


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoModelSerializer