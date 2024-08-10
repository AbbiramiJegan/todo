from django.shortcuts import render, get_object_or_404, redirect
from .models import todo

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:  # Ensure task is not empty
            todo.objects.create(todo_name=task)

    context = {
        'todos': todo.objects.all()
    }
    return render(request, 'todoapp/todo.html', context)

def delete_todo(request, id):
    if request.method == 'POST':
        get_object_or_404(todo, id=id).delete()
    return redirect('home')

def mark_finished(request, id):
    if request.method == 'POST':
        todo_item = get_object_or_404(todo, id=id)
        todo_item.status = True
        todo_item.save()
    return redirect('home')
