from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#Se importa el modulo HttpResponse para devolver una respuesta http simple.}

from polls.models import Question
from polls.models import Choice
from django.urls import reverse



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
    question = get_object_or_404(Question, pk=question_id)
    context = {"question" : question}
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question, 
               "error_message": "No elegiste una respuesta"}
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", context)

    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))