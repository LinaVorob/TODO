from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import BaseUser
from .serializers import UserModelSerializer, UserModelSerializerWithRole


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = BaseUser.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserModelSerializer()

    def get_serializer_class(self):
        print(f'Версия: {self.request.version}')
        if self.request.version == '2.0.1':
            return UserModelSerializerWithRole
        return UserModelSerializer

