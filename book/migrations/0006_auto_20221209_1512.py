# Generated by Django 3.2.12 on 2022-12-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_merge_0004_auto_20221209_1027_0004_auto_20221209_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
