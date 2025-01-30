from django.db import models

class UserRoleChoice(models.TextChoices):
    SUPERADMIN = ("superadmin", "superadmin")
    ADMIN = ("admin", "admin")
    TYUTOR = ("tyutor", "tyutor")


class TopshiriqRoleChoice(models.TextChoices):
    MAJBURIY = ("majburiy", "majburiy")
    QOSHIMCHA = ("qoshimcha", "qoshimcha")
    IXTIYORIY = ("ixtiyoriy", "ixtiyoriy")


