from rest_framework import serializers
from users.models import User
from tyutor.models import TyutorProfil, Fakultet


class FakultetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']



class TyutorProfilGetSerializer(serializers.ModelSerializer):
    fakultet = FakultetsSerializer()  # Faqatgina GET uchun detallarni ko'rsatadi
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)  
    last_name = serializers.CharField(source='user.last_name', read_only=True)  
      
    class Meta:
        model = TyutorProfil
        fields = ['id', 'username', 'first_name', 'last_name', 'user_role', 'fakultet', 'rasm']


class TyutorProfilPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  
    first_name = serializers.CharField(source='user.first_name', read_only=True)  
    last_name = serializers.CharField(source='user.last_name', read_only=True)  
    password = serializers.CharField(source='user.password', read_only=True)  

    class Meta:
        model = TyutorProfil
        fields = ['username', 'first_name', 'last_name', 'user_role', 'fakultet', 'rasm', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Parolni API javobida chiqarilmasligi uchun

