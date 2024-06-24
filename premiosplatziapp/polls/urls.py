from django.urls import path
from . import views

urlpatterns = [
    #La ruta raíz de la aplicación
    path("", views.index, name="index"),

    #/polls/id de la pregunta
    path("<int:question_id>/", views.details, name="index"),

    #/polls/id de la pregunta/results
    path("<int:question_id>/results", views.results, name="index"),

    #/polls/id de la pregunta/vote
    path("<int:question_id>/vote", views.vote, name="index")
]