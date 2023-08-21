from rest_framework import serializers
from .models import (
    Jamoatchlik_kengashi, Madaniyat_marifat, 
    Oquv_uslubiy,Akademik_litsey, Ilmiy_faoliyat, Yoshlar_bilan_ishlash
)

class Jamoatchlik_kengashiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jamoatchlik_kengashi
        fields = '__all__'

class Madaniyat_marifatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Madaniyat_marifat
        fields = '__all__'



class Oquv_uslubiySerializer(serializers.ModelSerializer):

    class Meta:
        model = Oquv_uslubiy
        fields = '__all__'


class Akademik_litseySerializer(serializers.ModelSerializer):

    class Meta:
        model = Akademik_litsey
        fields = '__all__'


class Ilmiy_faoliyatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ilmiy_faoliyat
        fields = '__all__'


class Yoshlar_bilan_ishlashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yoshlar_bilan_ishlash
        fields = '__all__'


