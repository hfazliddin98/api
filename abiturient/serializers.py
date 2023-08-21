from rest_framework import serializers
from .models import Abiturient_nomi, Abiturient_bolim, Abiturient_malumot


class Abiturient_nomiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abiturient_nomi
        fields = '__all__'


class Abiturient_bolimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abiturient_bolim
        fields = '__all__'

class Abiturient_malumotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abiturient_malumot
        fields = '__all__'