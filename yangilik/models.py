from django.db import models

# Create your models here.
class Yangilik(models.Model):
    title = models.CharField(max_length=1000, blank=True)
    body = models.TextField(blank=True, null=True)
    rasm = models.FileField(upload_to='yangilik/', blank=True)
    sana = models.DateTimeField(auto_now_add=True)