import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import UserRoleChoice

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    qr_code = models.ImageField(upload_to='qr_code', blank=True, null=True)
    parol = models.CharField(max_length=255, blank=True)




class AsosiyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True






