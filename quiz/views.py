from django.shortcuts import render
from .models import Quiz, Question
import datetime
from django.http import HttpResponse
from django.shortcuts import render

def list_quizzes(request):
    today = datetime.datetime.today()
    past_quizzes = Quiz.objects.filter(
        scheduled_at__lt=today
    )
    present_quizzes = Quiz.objects.filter(
        scheduled_at=today
    )
    future_quizzes = Quiz.objects.filter(
        scheduled_at__gt=today
    )
    return render(
        request,
        'index.html',
        {
            'past_quizzes': past_quizzes,
            'present_quizzes': present_quizzes, 
            'future_quizzes':future_quizzes
        }
    )

def show_quiz(request, quiz_id):
    try:
        questions = Question.objects.filter(quiz_id=quiz_id)
    except:
        return HttpResponse("No Questions in this Quiz!")
    else:
        return render(request, 'questions.html', {"questions": questions})