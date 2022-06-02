from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from tasks.models import Project, Todo
from .models import BaseUser
from .serializers import UserModelSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = BaseUser.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
