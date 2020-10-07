from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    scheduled_at = models.DateField()

    def __str__(self):
        return self.name


class Questions(models.Model):
    type = models.CharField(
        max_length=4,
        choices= [
            ['MCQ', 'Multiple Choice Questions'],
            ['TXT', 'Text']
        ]
    )
    image = models.ImageField(null=True, blank = True)
    ques = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.quiz.pk)+"-"+self.pk+"-"+self.ques

class Options(models.Model):
    choice_a = models.CharField(max_length=500)
    choice_b = models.CharField(max_length=500)
    choice_c = models.CharField(max_length=500)
    choice_d = models.CharField(max_length=500)
    answer = models.TextField()
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.question.pk)+self.answer

class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = ['user', 'quiz']

    def __str__(self):
        return str(self.user.pk)+'-'+str(self.quiz.pk)+'-'+str(self.score)

