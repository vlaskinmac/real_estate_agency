# Generated by Django 2.2.24 on 2022-03-19 08:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220319_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='author_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
