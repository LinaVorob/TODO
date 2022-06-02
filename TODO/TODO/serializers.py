from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.reverse import reverse
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from mainapp.serializers import UserModelSerializer
from tasks.models import Project, Todo


class ProjectModelSerializer(ModelSerializer):
    # user = UserModelSerializer()

    class Meta:
        model = Project
        # fields = ['name', 'repohref', 'user', 'update_at']
        fields = '__all__'



class ToDoModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer()
    project = ProjectModelSerializer()

    class Meta:
        model = Todo
        fields = ['project', 'text', 'author', 'users', 'status', 'updated_at']
