from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from mainapp.views import UserViewSet
from tasks.views import ProjectViewSet, TodoViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # re_path(r'^(?P<version>\d\.\d\.\d)/users/$', UserViewSet.as_view({'get': 'list'}))
    path('1.1.1/users/', include('mainapp.urls', namespace='1.1.1')),
    path('2.2.2/users/', include('mainapp.urls', namespace='2.2.2'))
]
