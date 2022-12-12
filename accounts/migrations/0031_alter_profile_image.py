# Generated by Django 3.2.12 on 2022-12-12 17:31

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='media/profile/'),
        ),
    ]
