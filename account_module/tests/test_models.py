from django.test import TestCase
from account_module.models import User

class TestModels(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            email='test123@test.com',
            username='Test1',
            profile_picture='uploads/Profiles/profile/chun-li.jpg',
            channel_banner='uploads\Profiles\Channel_banner\mortal-kombat-banner.jpg',
            password='1234k1234_Kk'
        )

    def test_user_creation(self):
        self.assertEqual(self.test_user.email, 'test123@test.com')
        self.assertEqual(self.test_user.username, 'Test1')
        self.assertEqual(self.test_user.profile_picture, 'uploads/Profiles/profile/chun-li.jpg')
        self.assertEqual(self.test_user.channel_banner, 'uploads\Profiles\Channel_banner\mortal-kombat-banner.jpg')
        self.assertEqual(self.test_user.password, '1234k1234_Kk')
