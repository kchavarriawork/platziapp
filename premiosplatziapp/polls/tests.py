#Importes de Python
import datetime


#Importes de Django
from django.test import TestCase
from django.utils import timezone

#Importe de Models
from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_future_question(self):
        """was_published_recently returns false for questions whose pub_date in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es ek nehir Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)




 