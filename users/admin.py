from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = [
        'username', 'first_name', 'last_name',
        'is_superuser', 'is_active'
    ]


