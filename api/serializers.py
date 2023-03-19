from rest_framework import serializers
from .models import Fayl

class FaylSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fayl
        fields = '__all__'
