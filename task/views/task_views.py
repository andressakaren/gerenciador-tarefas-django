from django.shortcuts import render
from task.models import Task

def index(request):
    
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
    }
    
    return render(
        request,
        'task/index.html',
        context,
    )