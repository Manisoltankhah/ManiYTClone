from django.test import TestCase, Client
from django.urls import reverse, resolve
from account_module.models import User
from channel_module.views import ChannelHomeView

class TestViews(TestCase):
    def setUp(self):
        self.channel = User.objects.create(
            username='Channel 1',
            profile_picture='uploads\Profiles\profile\chun-li.jpg',
            about_user='Test Channel',
            channel_banner='uploads\Profiles\Channel_banner\mortal-kombat-banner.jpg',
            slug='Channel-1',
        )
        self.client = Client()

        self.channel_home_page_url = reverse('channel-home-page', args=[self.channel.slug])

    def test_Channel_home_page_GET(self):
        response = self.client.get(self.channel_home_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('channel-page.html')