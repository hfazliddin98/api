from django.contrib import admin
from .models import Jamoatchlik_kengashi, Madaniyat_marifat, Oquv_uslubiy, Akademik_litsey, Ilmiy_faoliyat, Yoshlar_bilan_ishlash

admin.site.register([
    Jamoatchlik_kengashi,
    Madaniyat_marifat,
    Oquv_uslubiy,
    Akademik_litsey,
    Ilmiy_faoliyat,
    Yoshlar_bilan_ishlash
])
