from django.contrib import admin


from polls.models import Question
from .models import Choice


#Clase que permite agregar las respuestas de las preguntas
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


#Clase que define el orden de las preguntas
class QuestionAdminOrder(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]

    #Agrega y ordena los campos de Questions
    list_display = ("question_text", "pub_date", "was_published_recently")
    
    #Agrega un filtrado por el campo pub_date
    list_filter = ["pub_date"]

    #Agrega una barra de búsqueda y se filtrará por la pregunta
    search_fields = ["question_text"]


# Register your models here.
admin.site.register(Question, QuestionAdminOrder)
admin.site.register(Choice)
