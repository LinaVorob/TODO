from rest_framework.serializers import HyperlinkedModelSerializer

from tasks.models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        # fields = ['name', 'repohref', 'user', 'update_at']
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['project', 'text', 'author', 'users', 'status', 'updated_at']
