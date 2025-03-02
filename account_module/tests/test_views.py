from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from account_module.forms import RegisterForm, LoginForm

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('sign_up')
        self.login_page = reverse('login-page')
        self.home_url = reverse('home_page')
        self.user_data = {
            'email': 'test@example.com',
            'username': 'test123',
            'password': 'testpassword123'
        }
        self.existing_user = User.objects.create_user(
            email='existing@gmail.com',
            username='existing_user',
            password='existingpass123',
            is_active=True
        )
        self.user_login_data = {
            'email': 'existing@gmail.com',
            'password': 'existingpass123'
        }
        self.invalid_data = {
            'email': 'existing@gmail.com',
            'password': 'wrongpassword'
        }

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign-up-page.html')
        self.assertIsInstance(response.context['register_form'], RegisterForm)

    def test_login_view_get(self):
        response = self.client.get(self.login_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_page.html')
        self.assertIsInstance(response.context['login_form'], LoginForm)

    def test_register_view_post_success(self):
        User.objects.filter(email='test@example.com').delete()
        response = self.client.post(self.register_url, data=self.user_data)
        if response.context and 'register_form' in response.context:
            print(response.context['register_form'].errors)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_page)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_login_view_POST_success(self):
        response = self.client.post(self.login_page, self.user_login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)
        self.assertTrue('_auth_user_id' in self.client.session)