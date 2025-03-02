from django.test import TestCase
from django.urls import reverse, resolve
from account_module.models import User
from channel_module.views import ChannelHomeView

class TestUrl(TestCase):

    def test_channel_home_view(self):
        channel = User.objects.create(
            username = 'Channel 1',
            profile_picture = 'uploads\Profiles\profile\chun-li.jpg',
            about_user = 'Test Channel',
            channel_banner = 'uploads\Profiles\Channel_banner\mortal-kombat-banner.jpg',
            slug ='Channel-1',
        )
        url = reverse('channel-home-page', args=[channel.slug])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ChannelHomeView)