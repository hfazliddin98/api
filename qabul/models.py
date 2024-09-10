from django.db import models

class QabulAriza(models.Model):
    familya = models.CharField(max_length=255, blank=True)
    ism = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    nomer = models.CharField(max_length=255, blank=True)
    tahsil_olgan = models.CharField(max_length=255, blank=True)
    fuqaroligi = models.CharField(max_length=255, blank=True)
    telegram_name = models.CharField(max_length=255, blank=True)
    wahatsap_name = models.CharField(max_length=255, blank=True)