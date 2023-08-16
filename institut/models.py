from django.db import models

# Create your models here.
class Inistitut(models.Model):
    nomi = models.CharField(max_length=100)    


class Rasm(models.Model):
    nomi = models.ForeignKey('Inistitut', on_delete=models.CASCADE)
