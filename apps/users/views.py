from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(username=username)
                user.set_password(password1)
                user.save()
                user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect('index')
            except:
                messages.error(request, 'Not correct some value')
        else:
            messages.error(request, 'Not correct password')
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error(request, 'Not correct login or password')
    return render(request, 'login.html')