from rest_framework import serializers
from .models import Yangilik



class YangilikSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yangilik
        fields = '__all__'

