from rest_framework.serializers import HyperlinkedModelSerializer
from .models import BaseUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['username', 'firstname', 'lastname', 'email']