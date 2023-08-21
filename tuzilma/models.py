from django.db import models


class Yonalish(models.Model):
    yonalish_nomi = models.CharField(max_length=100, blank=True)

class Bolim(models.Model):
    bolim_nomi = models.CharField(max_length=100, blank=True)

class Rahbar(models.Model):
    yonalish_id = models.CharField(max_length=100, blank=True)
    bolim_id = models.CharField(max_length=100, blank=True)
    lavozim = models.CharField(max_length=100, blank=True)
    darajasi = models.CharField(max_length=100, blank=True)
    f_i_sh = models.CharField(max_length=100, blank=True)
    telefon = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)
    rasm = models.FileField(upload_to='rahbarlar/', blank=True)