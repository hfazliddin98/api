from rest_framework import serializers
from .models import Inistitut_kengashi, Institut_haqida, Institut_tuzulmasi, Qabulxona, Rekvizidlar

class Inistitut_kengashiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inistitut_kengashi
        fields = '__all__'


class Institut_haqidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institut_haqida
        fields = '__all__'


class Institut_tuzulmasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institut_tuzulmasi
        fields = '__all__'


class QabulxonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qabulxona
        fields = '__all__'



class RekvizidlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rekvizidlar
        fields = '__all__'