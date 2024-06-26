from django.urls import path
from . import views

#Declaración de variable base para el enrutamiento
app_name = "polls"

urlpatterns = [
    #La ruta raíz de la aplicación
    path("", views.index, name="index"),

    #/polls/id de la pregunta
    path("<int:question_id>/details", views.details, name="details"),

    #/polls/id de la pregunta/results
    path("<int:question_id>/results", views.results, name="results"),

    #/polls/id de la pregunta/vote
    path("<int:question_id>/vote", views.vote, name="vote")
]