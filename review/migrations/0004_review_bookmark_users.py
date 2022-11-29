# Generated by Django 3.2.12 on 2022-11-29 05:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_auto_20221128_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='bookmark_users',
            field=models.ManyToManyField(related_name='bookmark_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
