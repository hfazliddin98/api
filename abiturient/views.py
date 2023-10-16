from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Abiturient_nomi, Abiturient_bolim, Abiturient_malumot
from .serializers import Abiturient_nomiSerializer, Abiturient_bolimSerializer, Abiturient_malumotSerializer



class Abiturient_nomiViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Abiturient_nomi.objects.all()
    serializer_class = Abiturient_nomiSerializer
    

class Abiturient_bolimViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Abiturient_bolim.objects.all()
    serializer_class = Abiturient_bolimSerializer


class Abiturient_malumotViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Abiturient_malumot.objects.all()
    serializer_class = Abiturient_malumotSerializer


