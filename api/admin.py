from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Fayl

# admin.site.register(Fayl)
admin.site.unregister(Group)