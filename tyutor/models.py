from django.db import models
from users.models import User, AsosiyModel
from tyutor.choices import UserRoleChoice




class Fakultet(AsosiyModel):
    name = models.CharField(max_length=255)

class TyutorProfil(AsosiyModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=30, choices=UserRoleChoice.choices)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='users', blank=True, null=True)
