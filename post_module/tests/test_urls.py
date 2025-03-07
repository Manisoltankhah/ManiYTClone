from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from account_module.models import User
from post_module.models import Post, Playlist, PostComments
from post_module.views import PostDetailPage, PlaylistDetailView, AddComment, \
    comment_edit, delete_comment, PostLike, PostDisLike

class TestUrls(TestCase):
    # Testing post detail page URL
    def test_post_detail_page_url_is_resolved(self):
        test = Post.objects.create(
            title='post',
            description="posting",
            slug='post1',
            thumbnail=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
        )
        url = reverse('post_detail_page', args={(test.slug)})
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, PostDetailPage)

    # Testing playlist detail page URL
    def test_playlist_detail_page_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        test = Playlist.objects.create(
            title='playlist',
            channel_id=test_user.id,
            slug='playlist1'
        )
        url = reverse('playlist_detail_page', args={(test.slug), (test_post.slug)})
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, PlaylistDetailView)

    # Testing add comment URL
    def test_add_post_comment_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        url = reverse('add_post_comment', args=[test_post.slug, test_post.id])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AddComment)

    # Testing edit comment URL
    def test_edit_post_comment_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        url = reverse('edit_post_comment', args=[test_post.slug, test_post.id])
        print(resolve(url))
        self.assertEqual(resolve(url).func, comment_edit)

    # Testing delete comment URL
    def test_delete_post_comment_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        url = reverse('delete_post_comment', args=[test_post.slug, test_post.id])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_comment)

    # Testing post like URL
    def test_post_like_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        url = reverse('post_like', args=[test_post.slug])
        print(resolve(url))
        self.assertEqual(resolve(url).func, PostLike)

    # Testing post dislike URL
    def test_post_dislike_url_is_resolved(self):
        test_user = User.objects.create(
            email='test@test.com',
            username='Test'
        )
        test_post = Post.objects.create(
            title='post',
            description="posting",
            slug='post1'
        )
        url = reverse('post_dislike', args=[test_post.slug])
        print(resolve(url))
        self.assertEqual(resolve(url).func, PostDisLike)