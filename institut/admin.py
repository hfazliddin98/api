from django.contrib import admin
from .models import Inistitut_kengashi, Institut_haqida, Institut_tuzulmasi, Rekvizidlar, Qabulxona


admin.site.register([
    Inistitut_kengashi, Institut_haqida,
    Institut_tuzulmasi, Rekvizidlar,Qabulxona
])