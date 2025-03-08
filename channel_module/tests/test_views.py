from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from account_module.models import User
from channel_module.forms import PlaylistCreationForm
from channel_module.views import ChannelHomeView, CreatePlaylistView
from django.core.files.uploadedfile import SimpleUploadedFile

from post_module.models import Post, Playlist, PlaylistVideo


class TestViews(TestCase):
    def setUp(self):
        self.channel = User.objects.create(
            username='Channel-1',
            profile_picture='uploads\Profiles\profile\chun-li.jpg',
            about_user='Test Channel',
            channel_banner='uploads\Profiles\Channel_banner\mortal-kombat-banner.jpg',
            slug='Channel-1',  # Use a valid slug format
        )

        self.post1 = Post.objects.create(
            title='post1',
            description="posting",
            slug='post1',
            thumbnail='uploads/thumbnails/Atomic_Heart_twins_video_game_characters-2237718.jpg',
            video='uploads/uploaded_videos/I_LOVE_THIS_DRESS.mp4',
            channel=self.channel,
            is_active=True
        )

        self.post2 = Post.objects.create(
            title='post2',
            description="posting",
            slug='post2',
            thumbnail='uploads/thumbnails/Atomic_Heart_twins_video_game_characters-2237718.jpg',
            video='uploads/uploaded_videos/I_LOVE_THIS_DRESS.mp4',
            channel=self.channel,
            is_active=True
        )
        self.client = Client()
        self.factory = RequestFactory()

        self.channel_home_page_url = reverse('channel-home-page', args=[self.channel.slug])

    def test_Channel_home_page_GET(self):
        response = self.client.get(self.channel_home_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('channel-page.html')

    def test_user_edit_POST(self):
        self.client.force_login(self.channel)
        edited_user_data = {
            'username': 'Channel2',
            'profile_picture': 'uploads/Profiles/profile/17369481500301.jpg',
            'about_user': 'Lovely Channel',
            'channel_banner': 'uploads/Profiles/Channel_banner/17369481500471.jpg',
            'slug': 'Channel-2',
        }
        response = self.client.post(reverse('user-panel-page', args=[self.channel.slug]), data=edited_user_data)

        self.channel.refresh_from_db()
        self.assertEqual(self.channel.username, edited_user_data['username'])
        self.assertTrue(self.channel.profile_picture)
        self.assertEqual(self.channel.about_user, edited_user_data['about_user'])
        self.assertTrue(self.channel.channel_banner)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('channel-home-page', args=[self.channel.slug]))

    def test_form_valid(self):
        # Simulate a POST request with valid data
        data = {
            'title': 'My Playlist',
            'video': [str(self.post1.id), str(self.post2.id)]
        }
        request = self.factory.post(reverse('playlist-create-page', args=[self.channel.slug]), data)
        request.user = self.channel

        # Instantiate the view
        view = CreatePlaylistView()
        view.request = request

        # Instantiate the form with the POST data
        form = PlaylistCreationForm(data=data, user=self.channel)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

        # Call form_valid and check the saved object
        response = view.form_valid(form)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Retrieve the saved playlist
        playlist = Playlist.objects.first()
        self.assertIsNotNone(playlist)
        self.assertEqual(playlist.title, 'My Playlist')
        self.assertEqual(playlist.channel, self.channel)
        self.assertTrue(playlist.is_active)

        # Check that the videos are correctly associated
        self.assertQuerySetEqual(playlist.video.all().order_by('id'), [self.post1, self.post2], transform=lambda x: x)