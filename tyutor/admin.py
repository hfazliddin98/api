from django.contrib import admin
from tyutor.models import TyutorProfil, Fakultet


@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']

@admin.register(TyutorProfil)
class TyutorProfilAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user__username', 'user__first_name', 'user__last_name', 'user__parol']