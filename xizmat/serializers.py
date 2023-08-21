from rest_framework import serializers
from .models import Interaktiv_xizmatlar


class Interaktiv_xizmatlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interaktiv_xizmatlar
        fields = '__all__'

