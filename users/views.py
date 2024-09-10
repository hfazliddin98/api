from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):


    return redirect('v1/rest/swagger/')