from django.contrib import admin
from .models import User, Asosiy

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = [
        'username', 'first_name', 'last_name',
        'is_superuser', 'is_active'
    ]

@admin.register(Asosiy)
class AsosiyAdmin(admin.ModelAdmin):
    list_display  = ['id']
