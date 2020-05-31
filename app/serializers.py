from rest_framework import serializers
from .models import Question, Answer


class AnswerCreateSerializers(serializers.ModelSerializer):
    """Добавление ответа"""

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerListSerializers(serializers.ModelSerializer):
    """Добавление ответа"""

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionListSerializers(serializers.ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Question
        fields = ('title', 'date_start', 'date_close', 'text', 'answer_id')
