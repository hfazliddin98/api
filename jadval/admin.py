from django.contrib import admin
from .models import Talim_turi, Fakultet, Yonalish, Kurs, Jadval


@admin.register(Talim_turi)
class TalimUser(admin.ModelAdmin):
    list_display = [
        'id'
    ]

@admin.register(Fakultet)
class FakultetUser(admin.ModelAdmin):
    list_display = [
        'id'
    ]

@admin.register(Jadval)
class JadvalUser(admin.ModelAdmin):
    list_display = [
        'id'
    ]


@admin.register(Yonalish)
class YonalishUser(admin.ModelAdmin):
    list_display = [
        'id'
    ]

@admin.register(Kurs)
class KursUser(admin.ModelAdmin):
    list_display = [
        'id'
    ]

