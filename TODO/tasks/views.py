from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from TODO.serializers import ProjectModelSerializer, ToDoModelSerializer
from tasks.filters import ProjectFilter
from tasks.models import Project, Todo


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ToDOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDOLimitOffsetPagination
    filterset_fields = ['project']
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def destroy(self, request, *args, **kwargs):
        print(request)
        todo = get_object_or_404(Todo, pk=request['pk'])
        todo.status = 0
        todo.save()
