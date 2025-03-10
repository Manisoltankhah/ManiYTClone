# Generated by Django 3.2.23 on 2024-01-22 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0004_postviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postviews',
            options={'verbose_name': 'Blog visit', 'verbose_name_plural': 'Blog visits'},
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='postviews',
            name='ip',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='User IP'),
        ),
        migrations.AddField(
            model_name='postviews',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User View'),
        ),
    ]
