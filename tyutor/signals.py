# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from users.models import User
# from django.core.exceptions import ValidationError
# from .models import TyutorProfil

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
