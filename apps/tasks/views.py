from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime


def tasks(request):
    if request.method == "POST":
        content = request.POST.get('content')
        description = request.POST.get('description')
        time_str = request.POST.get('time')
        time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M')
        Task.objects.create(title=content, description=description, created_at=time)
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, 'base.html', {'tasks': tasks})
