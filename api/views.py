from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Fayl
from .serializers import FaylSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



class FaylViewSet(viewsets.ModelViewSet):
    queryset = Fayl.objects.all()
    serializer_class = FaylSerializer
    @csrf_exempt
    def my_view(request):
        response = HttpResponse('Hello, world!')
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
        return response


class FaylListView(generics.ListAPIView):
    queryset = Fayl.objects.all()
    serializer_class = FaylSerializer

class FaylCreateView(generics.CreateAPIView):
    queryset = Fayl.objects.all()
    serializer_class = FaylSerializer