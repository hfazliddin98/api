from django.db import models



class Rahbariyat(models.Model):
    fish = models.CharField(max_length=255, blank=True)
    lavozim = models.CharField(max_length=255, blank=True)
    rasm = models.FileField(upload_to='rahbariyat/', blank=True)
    nomer = models.CharField(max_length=100, blank=True)
