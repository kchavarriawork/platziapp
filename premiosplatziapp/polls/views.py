from django.shortcuts import render
from django.http import HttpResponse 
#Se importa el modulo HttpResponse para devolver una respuesta http simple.


# Create your views here.
def index(request):
    return HttpResponse("Pagina principal de Premios Platzi")


def details(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número: {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número: {question_id}")