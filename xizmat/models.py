from django.db import models

class Interaktiv_xizmatlar(models.Model):
    nomi = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)
