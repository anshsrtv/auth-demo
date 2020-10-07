from django.shortcuts import render
from .models import Quiz
import datetime
from django.http import HttpResponse
from django.shortcuts import render

def list_quizzes(request):
    today = datetime.datetime.today()
    past_quizzes = Quiz.objects.filter(
        scheduled_at__lt=today
    )
    print(str(past_quizzes[0].scheduled_at))
    present_quizzes = Quiz.objects.filter(
        scheduled_at=today
    )
    print(present_quizzes)
    future_quizzes = Quiz.objects.filter(
        scheduled_at__gt=today
    )
    print(future_quizzes)
    return render(request, 'index.html',{'past_quizzes': past_quizzes, 'present_quizzes': present_quizzes, 'future_quizzes':future_quizzes})