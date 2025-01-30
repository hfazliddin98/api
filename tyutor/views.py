from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from tyutor.models import TyutorProfil, Fakultet, Fayl, Topshiriq
from tyutor.serializers import TyutorProfilGetSerializer, TyutorProfilPostSerializer, TopshiriqSerializer


class TyutorProfilModelViewSet(ModelViewSet):
    queryset = TyutorProfil.objects.filter(user__is_superuser=False)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__username', 'user_role']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return TyutorProfilGetSerializer
        return TyutorProfilPostSerializer  # POST, PUT, PATCH uchun

    def create(self, request, *args, **kwargs):
        # Request ma'lumotlarini oling
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        user_role = request.data.get('user_role')  # Rol (agar kerak bo'lsa)
        rasm = request.data.get('rasm')
        fakultet_id = request.data.get('fakultet') 

        # Foydalanuvchi yaratish
        try:
            if User.objects.filter(username=username).exists():
                return Response({"detail": "Bunday username allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    parol=password
                )
                user.set_password(password)
                user.save()

                # Fakultet ob'ektini olish
                try:
                    fakultet = Fakultet.objects.get(id=fakultet_id)
                except Fakultet.DoesNotExist:
                    return Response({"detail": "Bunday Fakultet mavjud emas!"}, status=status.HTTP_400_BAD_REQUEST)

                if TyutorProfil.objects.filter(user=user).exists():
                    return Response({"detail": "Bunday user allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    tyutor = TyutorProfil.objects.create(
                        user=user,
                        user_role=user_role,
                        fakultet=fakultet,  
                        rasm=rasm  
                    )
                    # Javob qaytarish
                    serializer = TyutorProfilGetSerializer(tyutor)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"detail": f"Xatolik: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        


class TopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TopshiriqSerializer
    parser_classes = (MultiPartParser, FormParser)  # Fayllarni qabul qilish uchun
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
