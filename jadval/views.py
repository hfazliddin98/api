from django.shortcuts import render
from rest_framework import viewsets
from .models import Talim_turi, Fakultet, Yonalish, Kurs, Jadval
from .serializers import Talim_turiJadvalSerializer, FakultetJadvalSerializer,\
    YonalishJadvalSerializer, KursJadvalSerializer, JadvalSerializer



class Talim_turiJadvalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Talim_turi.objects.all()
    serializer_class = Talim_turiJadvalSerializer

class FakultetJadvalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Fakultet.objects.all()
    serializer_class = FakultetJadvalSerializer

class YonalishJadvalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Yonalish.objects.all()
    serializer_class = YonalishJadvalSerializer

class KursJadvalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Kurs.objects.all()
    serializer_class = KursJadvalSerializer

class JadvalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Jadval.objects.all()
    serializer_class = JadvalSerializer

