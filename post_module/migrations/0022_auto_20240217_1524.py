# Generated by Django 3.2.23 on 2024-02-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0021_auto_20240217_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='playlist',
            new_name='video',
        ),
        migrations.AddField(
            model_name='playlist',
            name='thumbnail_url',
            field=models.URLField(blank=True),
        ),
    ]
