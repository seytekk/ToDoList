from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime
from django.shortcuts import get_object_or_404


def get_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'cards.html', {'tasks': tasks})


def tasks(request):
    if request.method == "POST":
        content = request.POST.get('content')
        description = request.POST.get('description')
        time_str = request.POST.get('time')
        time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M')
        Task.objects.create(title=content, description=description, created_at=time)
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, 'cards.html', {'tasks': tasks})


def delete_task(request,task_id):
    if request.method == "POST":
        task=get_object_or_404(Task,id=task_id)
        task.delete()
        return redirect('/')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        new_title = request.POST.get("content", "").strip()  
        new_description = request.POST.get("description", "").strip()
        due_date_str = request.POST.get("due_date")

        if not new_title:
            return render(request, "update_task.html", {
                "task": task,
                "error": "Title can't be empty"
            })

        due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M') if due_date_str else None
        task.title = new_title
        task.description = new_description
        task.due_date = due_date
        task.save()
        return redirect('/')
    return render(request, "update_task.html", {"task": task})


def new_page(request):
    return render(request, 'create.html')

