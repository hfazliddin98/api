from rest_framework import serializers
from .models import Talaba_nomi, Talaba_malumot, Talaba_bolim



class Talaba_nomiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talaba_nomi
        fields = '__all__'


class Talaba_malumotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talaba_malumot
        fields = '__all__'


class Talaba_bolimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talaba_bolim
        fields = '__all__'

