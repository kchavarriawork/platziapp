from django.shortcuts import render
from django.http import HttpResponse 
#Se importa el modulo HttpResponse para devolver una respuesta http simple.}

from polls.models import Question


# Create your views here.


def index(request):
    question_list = Question.objects.all()
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)


def details(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número: {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número: {question_id}")