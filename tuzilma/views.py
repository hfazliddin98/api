from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Yonalish, Bolim, Rahbar 
from .serializers import YonalishSerializer, BolimSerializer, RahbarSerializer



class YonalishViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Yonalish.objects.all()
    serializer_class = YonalishSerializer
    


class BolimViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer
    


class RahbarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Rahbar.objects.all()
    serializer_class = RahbarSerializer
    