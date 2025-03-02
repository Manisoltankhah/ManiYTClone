from django.test import TestCase, Client
from django.urls import reverse, resolve

from account_module.models import User
from post_module.models import Post, Playlist


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(
            email='test@test.com',
            username='Test',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user.save()
        self.test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1',
            thumbnail='uploads/thumbnails/Atomic_Heart_twins_video_game_characters-2237718.jpg',
            video='uploads/uploaded_videos/I_LOVE_THIS_DRESS.mp4',
            channel_id=self.test_user.id
        )
        self.test_post.likes.add(self.test_user)
        self.test_post.save()

        self.playlist = Playlist.objects.create(
            title='Test Playlist',
            slug='test-playlist',
            channel_id=self.test_user.id
        )
        self.playlist.video.add(self.test_post)
        self.playlist.save()
        self.first_video = self.playlist.video.first()

        self.index_page_url = reverse('home_page')

    def test_index_page_GET(self):
        response = self.client.get(self.index_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')