from rest_framework.serializers import HyperlinkedModelSerializer
from .models import BaseUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['uuid', 'username', 'firstname', 'lastname', 'email']


class UserModelSerializerWithRole(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['uuid', 'username', 'firstname', 'lastname', 'email', 'is_superuser', 'is_staff']
