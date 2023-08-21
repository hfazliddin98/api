from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Interaktiv_xizmatlar
from .serializers import Interaktiv_xizmatlarSerializer




class Interaktiv_xizmatlarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Interaktiv_xizmatlar.objects.all()
    serializer_class = Interaktiv_xizmatlarSerializer
    
