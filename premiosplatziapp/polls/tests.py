#Importes de Python
import datetime

#Importes de Django
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

#Importe de Models
from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_future_question(self):
        """was_published_recently returns false for questions whose pub_date in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es ek nehir Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    """
    Create a question with the given "question_text" and publish it the given 
    number of days offset to now (negative for questions published in the past, 
    positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exist, an appopiate message is desplayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["question_list"], [])

    def test_past_question(self):
        """
        Questions with the pub_date in the past are
        displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["question_list"], [question])
        

    def test_future_question(self):
        """
        Questions with the pub_date in the future aren´t
        displayed on the index page
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["question_list"], [])