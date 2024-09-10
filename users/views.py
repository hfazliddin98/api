from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):


    return redirect('v1/rest/docs/')