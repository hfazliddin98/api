from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from. models import Rahbariyat
from .serializers import RahbariyatSerializer



class RahbariyatViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatSerializer
