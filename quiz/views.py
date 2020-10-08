from django.shortcuts import render, redirect
from .models import Quiz, Question, Attempt, Answer
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('list_quiz')

@login_required(login_url='login')
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


@login_required(login_url='login')
def show_quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk = quiz_id)
    except:
        return HttpResponse("No such Quiz exists!")
    else:
        try:
            questions = Question.objects.filter(quiz_id=quiz_id)
            answers = Answer.objects.filter(user=request.user)
        except:
            return HttpResponse("No Questions in this Quiz!")
        else:
            attempt = Attempt.objects.get_or_create(
                user=request.user,
                quiz=quiz
            )
            print(attempt[0].created_at)
            print(now())
            if now()>attempt[0].created_at+timedelta(minutes=quiz.duration_in_minutes):
                return HttpResponse("<div align='center'>Quiz Already Attempted! Your Score was "+str(attempt[0].score)+"<br/><br/><a href='/list/'>Home</a>")
            else:
                minutes=attempt[0].created_at+timedelta(minutes=quiz.duration_in_minutes)-now()
                return render(request, 'questions.html', {"minutes": round(minutes.total_seconds()/60,2), "questions": questions,"answers": answers, "attempt": attempt[0]})

@login_required(login_url='login')
def check_answer(request, question_id):
    try:
        question = Question.objects.filter(pk=question_id).first()
    except:
        return HttpResponse("No such question exists!")
    else:
        if request.method=='POST':
            attempt = Attempt.objects.get_or_create(
                quiz=question.quiz,
                user= request.user
            )[0]
            print(question)
            answer = Answer.objects.filter(user = request.user, question = question)
            print(answer)
            if not answer:
                try:
                    answer = Answer.objects.create(user = request.user, question = question, resp=request.POST['answer'])
                except:
                    return redirect('show_quiz', quiz_id=question.quiz.pk)
                if answer.resp==question.ans:
                    attempt.score+=20
                    print(attempt.score)
                    attempt.save()
                    return redirect('show_quiz', quiz_id=question.quiz.pk)
                else:
                    return redirect('show_quiz', quiz_id=question.quiz.pk)
            else:
                return redirect('show_quiz', quiz_id=question.quiz.pk)