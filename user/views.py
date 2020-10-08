from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
   if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_quiz')
   else:
       form = SignupForm()
   return render(request,'signup.html',{'form':form})

def log_in(request):
   if request.method == 'POST':
       user=authenticate(request,username=request.POST['username'],
       password=request.POST['password'])
       print(user)
       if user is not None:
           login(request,user)
           return redirect('list_quiz')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('login')
   else:
       form = AuthenticationForm()
       return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')