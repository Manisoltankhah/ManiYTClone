from django.test import TestCase
from account_module.models import User
from post_module.models import Post, Playlist, PostComments

class TestModels(TestCase):

    def setUp(self):  # Correct method name
        self.test_user1 = User.objects.create(
            email='test123@test.com',
            username='Test1',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user2 = User.objects.create(
            email='test456@test.com',
            username='Test2',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user3 = User.objects.create(
            email='test789@test.com',
            username='Test3',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user4 = User.objects.create(
            email='test135@test.com',
            username='Test4',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user5 = User.objects.create(
            email='test246@test.com',
            username='Test5',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.test_user1.save()
        self.post1 = Post.objects.create(
            title='post 1',
            description="posting",
            thumbnail='uploads/thumbnails/Atomic_Heart_twins_video_game_characters-2237718.jpg',
            video='uploads/uploaded_videos/I_LOVE_THIS_DRESS.mp4',
            channel_id=self.test_user1.id,
            is_active=True,
            created_date='2025-02-01',
        )
        self.post1.likes.add(self.test_user1)
        self.post1.likes.add(self.test_user3)
        self.post1.dislike.add(self.test_user2)
        self.post1.save()

        self.playlist = Playlist.objects.create(
            title= 'playlist 1',
            channel= self.test_user1,
            is_active = True,
            thumbnail_url = self.post1.thumbnail.url,
        )
        self.playlist.video.add(self.post1)
        self.playlist.save()

        self.comment1 = PostComments.objects.create(
            post = self.post1,
            user = self.test_user2,
            created_date = '2025-02-01',
            text= 'Commented'
        )

    def test_post_creation(self):
        self.assertEqual(self.post1.title, 'post 1')
        self.assertEqual(self.post1.description, 'posting')
        self.assertEqual(self.post1.channel, self.test_user1)
        self.assertTrue(self.post1.is_active)
        self.assertIsNotNone(self.post1.created_date, '2025-02-01')
        self.assertIsNotNone(self.post1.slug)  # Ensure the slug is auto-generated
        self.assertEqual(self.post1.thumbnail.name, 'uploads/thumbnails/Atomic_Heart_twins_video_game_characters-2237718.jpg')
        self.assertEqual(self.post1.video.name, 'uploads/uploaded_videos/I_LOVE_THIS_DRESS.mp4')

    def test_playlist_creation(self):
        self.assertEqual(self.playlist.title, 'playlist 1')
        self.assertEqual(self.playlist.thumbnail_url, self.post1.thumbnail.url)
        self.assertEqual(self.playlist.channel, self.test_user1)
        self.assertTrue(self.playlist.is_active)
        self.assertIsNotNone(self.playlist.slug, 'playlist-1')

    def test_post_comment_creation(self):
        self.assertEqual(self.comment1.post.title, 'post 1')
        self.assertEqual(self.comment1.user.id, self.test_user2.id)
        self.assertTrue(self.comment1.text, 'Commented')

    def test_post_is_assigned_slug_on_creation(self):
        self.assertEqual(self.post1.slug, 'post-1')

    def test_number_of_likes(self):
        self.assertEqual(self.post1.number_of_likes(), 2)
        self.post1.likes.add(self.test_user4)
        self.assertEqual(self.post1.number_of_likes(), 3)

    def test_number_of_dislikes(self):
        self.assertEqual(self.post1.number_of_dislikes(), 1)
        self.post1.dislike.add(self.test_user5)
        self.assertEqual(self.post1.number_of_dislikes(), 2)

