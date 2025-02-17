from django.shortcuts import render
from .models import Task


def get_tasks(request):
    tasks = Task.objects.filter(title='Решить задачу')
    return render(request, 'base.html', {'tasks': tasks})
