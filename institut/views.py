from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Inistitut_kengashi, Institut_haqida, Institut_tuzulmasi, Qabulxona, Rekvizidlar
from .serializers import (
    Inistitut_kengashiSerializer, Institut_haqidaSerializer, 
    Institut_tuzulmasiSerializer, QabulxonaSerializer, RekvizidlarSerializer
)

# Create your views here.


class Inistitut_kengashiViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Inistitut_kengashi.objects.all()
    serializer_class = Inistitut_kengashiSerializer

class Institut_haqidaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Institut_haqida.objects.all()
    serializer_class = Institut_haqidaSerializer

class Institut_tuzulmasiViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Institut_tuzulmasi.objects.all()
    serializer_class = Institut_tuzulmasiSerializer

class QabulxonaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Qabulxona.objects.all()
    serializer_class = QabulxonaSerializer

class RekvizidlarViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Rekvizidlar.objects.all()
    serializer_class = RekvizidlarSerializer

