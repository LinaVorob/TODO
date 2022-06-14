from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from mainapp.views import UserViewSet
from tasks.views import ProjectViewSet, TodoViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title='ToDoes',
        default_version='1.1.1',
        description='List of tasks for different project',
        contact=openapi.Contact(email='geekbrains@gb.com'),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('1.1.1/users/', include('mainapp.urls', namespace='1.1.1')),
    path('2.0.1/users/', include('mainapp.urls', namespace='2.0.1')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
