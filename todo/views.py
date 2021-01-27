from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib import messages

@login_required(login_url='/login/')
def list_todo(request):

    if request.method=='POST':
        title = request.POST['new-item']
        Todo(title = title, user = request.user).save()
        messages.success(request, message="New item added successfully!")    

    todos = Todo.objects.filter(user=request.user)

    return render(request, 'todo.html', {'todos': todos})
