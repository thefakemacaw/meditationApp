from django.shortcuts import render

# Create your views here.

#from Djangoproject: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the meditation app.")