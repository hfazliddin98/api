from rest_framework import serializers
from .models import Yonalish, Bolim, Rahbar



class YonalishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yonalish
        fields = '__all__'


class BolimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bolim
        fields = '__all__'


class RahbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rahbar
        fields = '__all__'

