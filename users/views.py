from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import Users, Binos
from .serializers import UserGetSerializer, UserPostSerializer, BinosSerializer


@csrf_exempt
def bosh_sahifa(request):
    return redirect('/swagger/')


