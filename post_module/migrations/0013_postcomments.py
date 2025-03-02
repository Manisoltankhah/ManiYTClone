# Generated by Django 3.2.23 on 2024-02-05 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0012_alter_post_channel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('text', models.TextField(verbose_name='comment Text')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_module.post', verbose_name='Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Blog Comment',
                'verbose_name_plural': 'Blog Comments',
            },
        ),
    ]
