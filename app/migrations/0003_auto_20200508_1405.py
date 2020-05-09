# Generated by Django 2.2.10 on 2020-05-08 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200508_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Голосов'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 14, 5, 51, 466692), verbose_name='Дата публикации'),
        ),
    ]
