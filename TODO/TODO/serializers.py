from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from mainapp.serializers import UserModelSerializer
from tasks.models import Project, Todo


class ProjectModelSerializer(ModelSerializer):
    user = UserModelSerializer

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer
    author = UserModelSerializer
    project = ProjectModelSerializer

    class Meta:
        model = Todo
        fields = ['uuid', 'project', 'text', 'author', 'users', 'status', 'updated_at']
