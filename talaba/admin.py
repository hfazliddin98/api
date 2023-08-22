from django.contrib import admin
from .models import Talaba_bolim, Talaba_malumot, Talaba_nomi

admin.site.register([
    Talaba_bolim, Talaba_malumot, Talaba_nomi
])
