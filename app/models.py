import datetime
from django.db import models


# class User(models.Model):
#     """Пользователь"""
#     name = models.CharField(max_length=50, verbose_name='Имя пользователя')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'


class Question(models.Model):
    """Опрос"""
    title = models.CharField(max_length=200, verbose_name="Название опроса")
    date_start = models.DateTimeField(verbose_name="Дата публикации",
                                      default=datetime.datetime.now())
    date_close = models.DateTimeField(verbose_name="Дата окончания")
    text = models.TextField(max_length=255, verbose_name='Текст вопроса')
    # is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


# class QuestionBody(models.Model):
#     """Конструктор опросника"""
#     answer_type_choices = (
#         ('1', 'Ответ текстом'),
#         ('2', 'Ответ с выбором одного варианта'),
#         ('3', 'Ответ с выбором нескольких вариантов'),
#     )
#
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Тема опроса:",
#                                  related_name='question_id')
#     choice_type = models.CharField(max_length=1, choices=answer_type_choices)
#     choice = models.CharField(max_length=255)
#     text = models.TextField(max_length=255, verbose_name='Создаем текст вопроса')
#
#     def __str__(self):
#         return self.choice
#
#     class Meta:
#         verbose_name = 'Конструктор опросов'
#         verbose_name_plural = 'Конструкторы опросов'


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
