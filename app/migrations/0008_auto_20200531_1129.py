# Generated by Django 2.2.10 on 2020-05-31 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200509_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 11, 29, 2, 966656), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=255, verbose_name='Текст вопроса'),
        ),
    ]
