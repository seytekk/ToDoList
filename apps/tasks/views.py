from django.shortcuts import render
from .models import Task


def get_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'cards.html', {'tasks': tasks})
