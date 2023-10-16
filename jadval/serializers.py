from rest_framework import serializers
from .models import Talim_turi, Fakultet, Yonalish, Kurs, Jadval

class Talim_turiJadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talim_turi
        fields = '__all__'

class FakultetJadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fakultet
        fields = '__all__'

class YonalishJadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yonalish
        fields = '__all__'

class KursJadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kurs
        fields = '__all__'


class JadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jadval
        fields = '__all__'


