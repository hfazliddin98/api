import os
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from users.models import User
from django.core.exceptions import ValidationError
from tyutor.models import TyutorProfil, Fayl

# @receiver(post_save, sender=TyutorProfil)
# def create_user_from_profile(sender, instance, created, **kwargs):
#     if created and instance.user is None:  # Agar foydalanuvchi hali mavjud bo'lmasa
#         # Foydalanuvchini yaratish
#         try:
#             print(instance)
#             user = User.objects.create(
#                 username=instance.username,  # User nomini TyutorProfil modelidan olish
#                 first_name=instance.first_name,  # Ism
#                 last_name=instance.last_name,  # Familiya
#             )
#             # Parolni shifrlash
#             user.set_password(instance.password)
#             user.save()

#             # TyutorProfilga foydalanuvchi o'rnatish
#             instance.user = user
#             instance.save()

#         except Exception as e:
#             raise ValidationError(f"Foydalanuvchi yaratishda xato yuz berdi: {e}")


@receiver(post_delete, sender=Fayl)
def delete_file_from_storage(sender, instance, **kwargs):
    """ Fayl modeli o‘chiriganda, bog‘langan faylni `media/` dan ham o‘chirish """
    if instance.file:  # Fayl mavjudligini tekshirish
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)  # Faylni o‘chirish