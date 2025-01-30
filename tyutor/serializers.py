from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.serializers import CharField, SerializerMethodField, ModelSerializer
from users.models import User
from tyutor.models import TyutorProfil, Fakultet, Fayl, Topshiriq


class FakultetsSerializer(ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']



class TyutorProfilGetSerializer(ModelSerializer):
    fakultet = FakultetsSerializer()  # Faqatgina GET uchun detallarni ko'rsatadi
    username = CharField(source='user.username', read_only=True)
    first_name = CharField(source='user.first_name', read_only=True)  
    last_name = CharField(source='user.last_name', read_only=True)  

    class Meta:
        model = TyutorProfil
        fields = ['id', 'username', 'first_name', 'last_name', 'user_role', 'fakultet', 'rasm']


class TyutorProfilPostSerializer(ModelSerializer):
    username = CharField(source='user.username', read_only=True)  
    first_name = CharField(source='user.first_name', read_only=True)  
    last_name = CharField(source='user.last_name', read_only=True)  
    password = CharField(source='user.password', read_only=True)  

    class Meta:
        model = TyutorProfil
        fields = ['username', 'first_name', 'last_name', 'user_role', 'fakultet', 'rasm', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Parolni API javobida chiqarilmasligi uchun



class FaylSerializer(ModelSerializer):
    class Meta:
        model = Fayl
        fields = ['id', 'file']



class TopshiriqSerializer(ModelSerializer):
    fayllar = FaylSerializer(many=True, read_only=True, required=False)  # Fayllarni yaratishda qabul qilish uchun

    class Meta:
        model = Topshiriq
        fields = ['id', 'title', 'fayllar']


    def create(self, validated_data):
        files_data = self.context['request'].FILES.getlist('fayllar')  # Fayllarni olish
        topshiriq = Topshiriq.objects.create(**validated_data)  # Topshiriq yaratish

        for file in files_data:  # Fayllarni bog‘lash
            Fayl.objects.create(file=file, topshiriq=topshiriq)

        return topshiriq
    
