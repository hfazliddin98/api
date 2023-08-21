from django.db import models

class Talaba_bolim(models.Model):
    nomi = models.CharField(max_length=100, blank=True)

class Talaba_nomi(models.Model):
    tur_nomi = models.CharField(max_length=100, blank=True)
    bolim = models.CharField(max_length=100, blank=True)


class Talaba_malumot(models.Model):
    bolim_nomi = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True, null=True)
    fayl = models.FileField(upload_to='malumot/', blank=True)

