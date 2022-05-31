from django.contrib import admin

# Register your models here.
from mainapp.models import BaseUser

admin.site.register(BaseUser)