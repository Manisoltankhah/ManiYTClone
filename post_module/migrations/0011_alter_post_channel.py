# Generated by Django 3.2.23 on 2024-01-22 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0010_alter_post_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]
