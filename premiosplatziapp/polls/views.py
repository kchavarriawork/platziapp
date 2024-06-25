from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
#Se importa el modulo HttpResponse para devolver una respuesta http simple.}

from polls.models import Question


# Create your views here.


def index(request):
    question_list = Question.objects.all()
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question" : question}
    return render(request, "polls/details.html", context)


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas vot ando a la pregunta número: {question_id}")