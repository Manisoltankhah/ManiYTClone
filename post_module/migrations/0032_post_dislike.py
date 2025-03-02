# Generated by Django 3.2.23 on 2024-08-27 14:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0031_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='Post_dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
