from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Yangilik
from .serializers import YangilikSerializer


class YangilikViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSerializer
    
