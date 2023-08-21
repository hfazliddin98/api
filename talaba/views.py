from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Talaba_nomi, Talaba_bolim, Talaba_malumot
from .serializers import Talaba_nomiSerializer, Talaba_malumotSerializer, Talaba_bolimSerializer


class Talaba_nomiViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Talaba_nomi.objects.all()
    serializer_class = Talaba_nomiSerializer
    

class Talaba_bolimViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Talaba_bolim.objects.all()
    serializer_class = Talaba_bolimSerializer
    

class Talaba_malumotViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Talaba_malumot.objects.all()
    serializer_class = Talaba_malumotSerializer
    
