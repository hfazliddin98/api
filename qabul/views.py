from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import QabulAriza
from .serializers import QabulArizaSerializer



class QabulArizaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = QabulAriza.objects.all()
    serializer_class = QabulArizaSerializer
    



    