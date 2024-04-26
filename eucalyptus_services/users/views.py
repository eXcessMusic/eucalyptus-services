from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')

    return render(request, 'users/register.html', {'form': RegisterForm})

def log_in(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_form = form.cleaned_data['username']
            password_form = form.cleaned_data['password']
            user = authenticate(request, username=username_form, password=password_form)
            if user:
                login(request,user)
                messages.success(request,f"Bienvenue {username_form}!")
                return redirect('article_list')
            
    return render(request, 'users/login.html', {'form': LoginForm})

def log_out(request):
    logout(request)
    return redirect('article_list')

