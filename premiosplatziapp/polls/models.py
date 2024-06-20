from django.db import models

# Create your models here.
#Aquí se crean las tablas necesarias para cada aplicación

class Question(models.Model):
    id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
