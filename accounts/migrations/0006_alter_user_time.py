# Generated by Django 3.2.12 on 2022-11-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20221128_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time',
            field=models.CharField(choices=[('오전', '오전 : 06:00 ~ 11:59'), ('오후', '오후 : 12:00 ~ 17:59'), ('저녁', '저녁 : 18:00 ~ 23:59')], max_length=20, null=True),
        ),
    ]
