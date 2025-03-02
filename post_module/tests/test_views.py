from django.db.migrations import swappable_dependency
from django.template.context_processors import request
from django.template.defaulttags import comment
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from account_module.models import User
from post_module import views
from post_module.models import Post, Playlist, PostComments


class TestViews(TestCase):

    def setUp(self):
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
            channel=self.test_user
        )
        self.test_post.likes.add(self.test_user)
        self.test_post.save()

        self.playlist = Playlist.objects.create(
            title='Test Playlist',
            slug='test-playlist',
            channel_id=self.test_user.id
        )
        self.comment1 = PostComments.objects.create(
            post=self.test_post,
            user=self.test_user,
            created_date='2025-02-01',
            text='commenting'
        )
        self.playlist.video.add(self.test_post)
        self.playlist.save()
        self.first_video = self.playlist.video.first()

        self.client = Client()
        self.factory = RequestFactory()

        self.post_detail_page_url = reverse('post_detail_page', args=[self.test_post.slug])
        self.playlist_detail_page_url = reverse('playlist_detail_page', args=[self.playlist.slug, self.first_video.slug])
        self.add_comment_url = reverse('add_post_comment', kwargs={'slug':self.test_post.slug, 'pk':self.test_user.id})
        self.edit_post_comment = reverse('edit_post_comment', kwargs={'slug':self.test_post.slug, 'pk':self.test_user.id})
        self.delete_post_comment = reverse('delete_post_comment', kwargs={'slug':self.test_post.slug, 'pk':self.test_user.id})
        self.post_like_url = reverse('post_like', kwargs={'slug':self.test_post.slug})
        self.post_dislike_url = reverse('post_dislike', kwargs={'slug':self.test_post.slug})


    def test_post_detail_page_GET(self):
        response = self.client.get(self.post_detail_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail_page.html')

    def test_playlist_detail_GET(self):
        response = self.client.get(self.playlist_detail_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'playlist.html')

    def test_add_comment_GET(self):
        response = self.client.get(self.post_detail_page_url)
        self.assertEqual(response.status_code, 200)

    def test_editcomment_GET_request(self):
        request = self.factory.get(self.edit_post_comment)
        request.user = self.test_user
        response = views.comment_edit(request, slug=self.test_post.slug, pk=self.test_user.pk)

        self.assertEqual(response.status_code, 200)

    def test_like_post_GET(self):
        response = self.client.get(self.post_like_url)
        self.assertEqual(response.status_code, 404)

    def test_dislike_post_GET(self):
        response = self.client.get(self.post_dislike_url)
        self.assertEqual(response.status_code, 404)

    def test_add_comment_POST_adds_new_comment(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test_post32@test.com',
            profile_picture='uploads/Profiles/profile/chun-li.jpg'
        )
        self.client.login(username='testuser', password='testpassword')

        data = {
            'created_date': '2025-02-01',
            'text': 'commenting'
        }
        response = self.client.post(reverse('add_post_comment', args=[self.test_post.slug, self.test_user.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail_page', args=[self.test_post.slug]))

    def test_like_post_POST(self):
        # Simulate a POST request to like the post
        response = self.client.post(reverse('post_like', args=[self.test_post.slug]),{'post_id': self.test_post.id})
        self.assertEqual(response.status_code, 404)
        self.assertTrue(self.test_post.likes.filter(id=self.test_user.id).exists())

    def test_dislike_post_POST(self):
        response = self.client.post(reverse('post_dislike', args=[self.test_post.slug]),{'post_id': self.test_post.id})
        self.assertEqual(response.status_code, 404)
        self.assertTrue(self.test_post.likes.filter(id=self.test_user.id).exists())

    def test_editcomment_POST_request(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'created_date': '2025-02-01',
            'text': 'Updated Comment'
        }
        request = self.factory.post(self.edit_post_comment, data)
        response = views.comment_edit(request, slug=self.test_post.slug, pk=self.comment1.pk)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the post detail page
        self.assertEqual(response.url, reverse('post_detail_page', args=[self.test_post.slug]))

        # Check if the comment was updated
        updated_comment = PostComments.objects.get(pk=self.comment1.pk)
        self.assertEqual(updated_comment.text, 'Updated Comment')

    def test_delete_comment_POST_request(self):
        self.client.login(username='testuser', password='testpassword')
        request = self.factory.post(self.delete_post_comment)
        request.user = self.test_user  # Manually attach the user to the request

        # Call the view function
        response = views.delete_comment(request, pk=self.comment1.pk, slug=self.test_post.slug)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('post_detail_page', args=[self.test_post.slug]))

        # Check if the comment was deleted
        with self.assertRaises(PostComments.DoesNotExist):
            PostComments.objects.get(pk=self.comment1.pk)