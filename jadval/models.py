from django.db import models


class Jadval(models.Model):
    turi = models.CharField(max_length=10, blank=True)
    fakultet = models.CharField(max_length=10, blank=True)
    yonalish = models.CharField(max_length=10, blank=True)
    kurs = models.CharField(max_length=10, blank=True)
    rasm = models.FileField(upload_to='jadval/', blank=True)



class Talim_turi(models.Model):
    talim_turi = models.CharField(max_length=100)

class Fakultet(models.Model):
    fakultet_talim_turi_id = models.CharField(max_length=10)
    fakultet = models.CharField(max_length=100)

class Yonalish(models.Model):
    yonalish_talim_turi_id = models.CharField(max_length=10)
    yonalish_fakultet_id = models.CharField(max_length=10)
    yonalish = models.CharField(max_length=100)

class Kurs(models.Model):
    kurs_talim_turi_id = models.CharField(max_length=10)
    kurs_fakultet_id = models.CharField(max_length=10)
    kurs_yonalish_id = models.CharField(max_length=10)
    kurs = models.CharField(max_length=100)
