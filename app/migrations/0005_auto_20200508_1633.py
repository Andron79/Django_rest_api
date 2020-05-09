# Generated by Django 2.2.10 on 2020-05-08 13:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200508_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionbody',
            name='user_id',
        ),
        migrations.AddField(
            model_name='questionbody',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question_id', to='app.Question', verbose_name='Тема опроса:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 16, 32, 59, 532095), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_question',
            field=models.TextField(max_length=255, verbose_name='Описание опроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название опроса'),
        ),
        migrations.AlterField(
            model_name='questionbody',
            name='text',
            field=models.TextField(max_length=255, verbose_name='Создаем текст вопроса'),
        ),
    ]