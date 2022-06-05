from django.urls import path, include, re_path

from mainapp.views import UserViewSet

app_name = 'mainapp'

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'}))
]
