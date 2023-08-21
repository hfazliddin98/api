from django.db import models

class Jamoatchlik_kengashi(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)

class Madaniyat_marifat(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)

class Oquv_uslubiy(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)

class Akademik_litsey(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)

class Ilmiy_faoliyat(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)

class Yoshlar_bilan_ishlash(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    malumot = models.TextField(blank=True, null=True)