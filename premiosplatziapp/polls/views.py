from django.shortcuts import render
from django.http import HttpResponse 
#Se importa el modulo HttpResponse para devolver una respuesta http simple.


# Create your views here.
def index(request):
    return HttpResponse("Hello World")