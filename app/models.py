import datetime
from django.db import models


class Question(models.Model):
    """Опрос"""
    title = models.CharField(max_length=200, verbose_name="Название опроса")
    date_start = models.DateTimeField(verbose_name="Дата публикации",
                                      default=datetime.datetime.now())
    date_close = models.DateTimeField(verbose_name="Дата окончания")
    text = models.TextField(max_length=255, verbose_name='Текст вопроса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Answer(models.Model):
    """Вариант ответа на опрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Опросы:",
                                    related_name='answer_id')
    answer = models.CharField(max_length=200, verbose_name="Ответ")

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
