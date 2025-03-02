from django.test import TestCase
from django.urls import reverse, resolve
from account_module.views import RegisterView, LoginView

class TestUrls(TestCase):
    def test_register_url(self):
        url = reverse('sign_up')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_login_url(self):
        url = reverse('login-page')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, LoginView)
