from django.test import TestCase
from .models import FAQ

class FAQTests(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is Django?")
        self.assertEqual(faq.get_translated_question('hi'), faq.question_hi)


