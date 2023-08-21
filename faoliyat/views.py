from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Jamoatchlik_kengashi, Madaniyat_marifat, Oquv_uslubiy,
    Akademik_litsey, Ilmiy_faoliyat, Yoshlar_bilan_ishlash
)
from .serializers import (
    Jamoatchlik_kengashiSerializer, Madaniyat_marifatSerializer,Oquv_uslubiySerializer,
    Akademik_litseySerializer, Ilmiy_faoliyatSerializer,Yoshlar_bilan_ishlashSerializer
)



class Jamoatchlik_kengashiViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Jamoatchlik_kengashi.objects.all()
    serializer_class = Jamoatchlik_kengashiSerializer
    


class Madaniyat_marifatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Madaniyat_marifat.objects.all()
    serializer_class = Madaniyat_marifatSerializer
    


class Oquv_uslubiyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Oquv_uslubiy.objects.all()
    serializer_class = Oquv_uslubiySerializer
    


class Akademik_litseyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Akademik_litsey.objects.all()
    serializer_class = Akademik_litseySerializer
    


class Ilmiy_faoliyatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ilmiy_faoliyat.objects.all()
    serializer_class = Ilmiy_faoliyatSerializer
    


class Yoshlar_bilan_ishlashViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Yoshlar_bilan_ishlash.objects.all()
    serializer_class = Yoshlar_bilan_ishlashSerializer
    

