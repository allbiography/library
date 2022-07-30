from .models import *
from django.contrib.auth.models import User
from import_export import resources


class Programming_BookResource(resources.ModelResource):
    class Meta:
        model = Programming_Book


class UserResource(resources.ModelResource):
    class Meta:
        model = User









