from rest_framework.viewsets import ModelViewSet

from tasks.models import Project, Todo
from .models import BaseUser
from .serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = UserModelSerializer

