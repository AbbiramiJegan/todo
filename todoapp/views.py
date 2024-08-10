from django.shortcuts import render
from .models import todo

# Create your views here.

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(todo_name=task)
        new_todo.save()

    return render(request, 'todoapp/todo.html', {})
