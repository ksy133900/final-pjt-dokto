# Generated by Django 3.2.12 on 2022-12-12 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
