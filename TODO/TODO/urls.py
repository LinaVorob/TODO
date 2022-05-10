from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import UserViewSet
from tasks.views import ProjectViewSet, TodoViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),


]
