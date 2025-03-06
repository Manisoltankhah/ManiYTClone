from django.db import models
from django.utils.text import slugify
from account_module.models import User


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Post Title')
    thumbnail = models.ImageField(upload_to='uploads/thumbnails', verbose_name='Post Thumbnail')
    video = models.FileField(upload_to='uploads/uploaded_videos', verbose_name='Post Video')
    description = models.TextField(db_index=True, verbose_name='Post description')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='Post slug')
    is_active = models.BooleanField(default=False, verbose_name='is/is not active')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    channel = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creator', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='Post_like', blank=True)
    dislike = models.ManyToManyField(User, related_name='Post_dislike', blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislike.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Playlist(models.Model):
    title = models.CharField(max_length=100, verbose_name='Playlist Title')
    channel = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Playlist Channel')
    is_active = models.BooleanField(default=False, null=True, blank=True, verbose_name='is/is not active')
    thumbnail_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    video = models.ManyToManyField(Post, verbose_name='Video', through='PlaylistVideo')
    slug = models.SlugField(db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}/{self.channel}'

    class Meta:
        verbose_name = 'Post Playlist'
        verbose_name_plural = 'Posts Playlist'


class PlaylistVideo(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.DO_NOTHING)
    video = models.ForeignKey('Post', on_delete=models.DO_NOTHING)


class PostViews(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Post')
    ip = models.CharField(max_length=30, verbose_name='User IP', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User View', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.post.title} / {self.ip}'

    class Meta:
        verbose_name = 'Post visit'
        verbose_name_plural = 'Post visits'


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', unique=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    text = models.CharField(max_length=10000, verbose_name='comment Text')

    def __str__(self):
        return f'{self.post.slug}/{self.user}'

    class Meta:
        verbose_name = 'Post Comment'
        verbose_name_plural = 'Post Comments'



