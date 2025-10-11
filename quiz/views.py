from .models import Question
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def add_questions(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit(request):
    user_answers = request.data.get("answers", [])
    total_questions = len(user_answers)
    score = 0

    for ans in user_answers:
        q_id = ans.get('question_id')
        selected_option = ans.get('selected_option')
        question = Question.objects.get(id = q_id)

        if question.correct_option == selected_option:
            score += 1

    return Response({
        "total_questions":total_questions,
        "correct_answers":score,
    })

@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    return Response({'message':"User created!"}, status = status.HTTP_201_CREATED)
