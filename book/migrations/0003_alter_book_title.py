# Generated by Django 3.2.12 on 2022-12-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
