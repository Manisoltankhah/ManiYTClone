# Generated by Django 3.2.23 on 2024-03-06 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0029_alter_playlist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='Post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
