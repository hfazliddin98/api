from django.db import models

class Inistitut_kengashi(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    f_i_sh = models.CharField(max_length=100, blank=True)
    telefon = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True) 
    rasm = models.FileField(upload_to='institut_kengashi/', blank=True)


class Institut_haqida(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)
    rasm = models.FileField(upload_to='institut_haqida/', blank=True)


class Institut_tuzulmasi(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)
    rasm = models.FileField(upload_to='institut_haqida/', blank=True)


class Rekvizidlar(models.Model):
    inn = models.CharField(max_length=100, blank=True)
    okonx = models.CharField(max_length=100, blank=True)
    shxr = models.CharField(max_length=100, blank=True)
    royhatdan_otgan_sana = models.CharField(max_length=100, blank=True)
    manzil = models.CharField(max_length=100, blank=True)
    telefon = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=100, blank=True)
    gaznachi_hisob = models.CharField(max_length=100, blank=True)
    gaznachi_inn = models.CharField(max_length=100, blank=True)
    mfo = models.CharField(max_length=100, blank=True)
    ifut = models.CharField(max_length=100, blank=True)

class Qabulxona(models.Model):
    fish = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    telefon = models.CharField(max_length=100, blank=True)
    xabar = models.TextField(blank=True, null=True)