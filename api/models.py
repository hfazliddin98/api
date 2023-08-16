from django.db import models

class Fayl(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    fan = models.CharField(max_length=100)    
    sana = models.DateTimeField(auto_now_add=True)
    