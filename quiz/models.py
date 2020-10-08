from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    scheduled_at = models.DateField()
    duration_in_minutes = models.IntegerField(default=60)

    def __str__(self):
        return self.name


class Question(models.Model):
    type = models.CharField(
        max_length=4,
        choices= [
            ['MCQ', 'Multiple Choice Questions'],
            ['TXT', 'Text']
        ]
    )
    image = models.ImageField(upload_to="question", null=True, blank = True)
    ques = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    choice_a = models.CharField(max_length=500, null=True, blank=True)
    choice_b = models.CharField(max_length=500, null=True, blank=True)
    choice_c = models.CharField(max_length=500, null=True, blank=True)
    choice_d = models.CharField(max_length=500, null=True, blank=True)
    ans = models.TextField()

    def __str__(self):
        return str(self.quiz.pk)+"-"+str(self.pk)+"-"+self.ques

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'quiz']]

    def __str__(self):
        return str(self.user.pk)+'-'+str(self.quiz.pk)+'-'+str(self.score)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    resp = models.TextField()

    class Meta:
        unique_together = ['user', 'question']

    def __str__(self):
        return str(self.user.pk)+"_Q"+str(self.question.pk)+") "+str(self.resp)