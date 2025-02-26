
from django.shortcuts import render
from .models import Task

# Create your views here.

def todo_app(request):
    my_tasks = Task.objects.all(),
    return render(request, 'todo_app.html', {'my_tasks': my_tasks})