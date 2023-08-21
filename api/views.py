from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .models import Fayl
from .serializers import FaylSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



class FaylViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fayl.objects.all()
    serializer_class = FaylSerializer


