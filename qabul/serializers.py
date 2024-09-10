from rest_framework import serializers
from .models import QabulAriza



class QabulArizaSerializer(serializers.ModelSerializer):

    class Meta:
        model = QabulAriza
        fields = '__all__'



