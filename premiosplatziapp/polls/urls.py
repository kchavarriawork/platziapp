from django.urls import path
from . import views

#Declaración de variable base para el enrutamiento
app_name = "polls"

urlpatterns = [
    #La ruta raíz de la aplicación
    path("", views.IndexView.as_view(), name="index"),

    #/polls/id de la pregunta
    path("<int:pk>/details", views.DetailsView.as_view(), name="details"),

    #/polls/id de la pregunta/results
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),

    #/polls/id de la pregunta/vote
    path("<int:question_id>/vote", views.vote, name="vote")
]