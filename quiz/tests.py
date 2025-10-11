from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Question

class QuizAPITests(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.token_url = reverse('token_obtain_pair')
        self.questions_url = reverse('get_questions')
        self.submit_url = reverse('submit')

        self.user = User.objects.create_user(username='testuser', password='testpass123')

        Question.objects.create(
        text="What is 2 + 2?",
        option_a="3", option_b="4", option_c="5", option_d="6",
        correct_option="B"
        )
        Question.objects.create(
            text="Capital of France?",
            option_a="London", option_b="Berlin", option_c="Paris", option_d="Rome",
            correct_option="C"
        )
        
        questions = list(Question.objects.all())
        self.correct_answers = [
            {"question_id": questions[0].id, "selected_option": "B"},
            {"question_id": questions[1].id, "selected_option": "C"}
        ]

    def test_register_user(self):
        data = {"username": "newuser", "password": "newpass123"}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)

    def test_login_user(self):
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.token = response.data['access']

    def test_get_questions(self):
        response = self.client.get(self.questions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)

    def test_submit_quiz_authenticated(self):
        login_response = self.client.post(self.token_url, {
            "username": "testuser",
            "password": "testpass123"
        }, format='json')
        token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.post(self.submit_url, {"answers": self.correct_answers}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("correct_answers", response.data)
        self.assertEqual(response.data["correct_answers"], 2)  # ✅ Expect 2 correct answers
        self.assertIn("total_questions", response.data)
        self.assertEqual(response.data["total_questions"], 2)

    def test_submit_quiz_unauthenticated(self):
        response = self.client.post(self.submit_url, {"answers": self.correct_answers}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
