from django.shortcuts import render, get_object_or_404
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
    
def task(request, task_id):
    
    # single_tasks = Task.objects.get(id=task_id)
    single_task = get_object_or_404(Task, id=task_id)
    
    context = {
        'task': single_task,
    }
    
    return render(
        request,
        'task/task.html',
        context,
    )