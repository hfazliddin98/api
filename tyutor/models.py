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


class Topshiriq(AsosiyModel):
    title = models.CharField(max_length=255)
    

class Fayl(AsosiyModel):
    file = models.FileField(upload_to='topshiriq/')
    topshiriq = models.ForeignKey(Topshiriq, related_name='fayllar', on_delete=models.CASCADE)

class Baxo(AsosiyModel):
    