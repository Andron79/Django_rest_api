from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer
from .serializers import QuestionListSerializers, AnswerCreateSerializers, AnswerListSerializers


class QuestionListView(APIView):
    """Вывод списка опросов"""

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializers(questions, many=True)
        return Response(serializer.data)


class QuestionDetailView(APIView):
    """Вывод деталей опроса"""

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = QuestionListSerializers(question)
        return Response(serializer.data)


class AnswerCreateView(APIView):
    """Добавление ответа к опросу"""

    def post(self, request):
        answer = AnswerCreateSerializers(data=request.data)
        if answer.is_valid():
            answer.save()
        return Response(status=201)


class AnswerListView(APIView):
    """Вывод списка ответов"""

    def get(self, request):
        answer = Answer.objects.all()
        serializer = AnswerListSerializers(answer, many=True)
        return Response(serializer.data)
