# Generated by Django 3.2.23 on 2024-02-16 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0016_auto_20240209_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'verbose_name': 'Post Playlist', 'verbose_name_plural': 'Posts Playlist'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='playlist',
        ),
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_module.post', verbose_name='Playlist'),
        ),
    ]
