from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.text import slugify


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='Profiles/profile', verbose_name='profile_picture', null=True)
    about_user = models.TextField(null=True, blank=True, verbose_name='about_user')
    slug = models.SlugField(db_index=True, max_length=100, verbose_name='User_slug', blank=True, null=True)
    channel_banner = models.ImageField(upload_to='Profiles/Channel_banner', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
