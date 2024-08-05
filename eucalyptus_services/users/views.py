from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .views import CustomUserCreationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! You can now create your artist profile.")
            return redirect('artist_create')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def log_in(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_form = form.cleaned_data['username']
            password_form = form.cleaned_data['password']
            user = authenticate(request, username=username_form, password=password_form)
            if user:
                login(request,user)
                messages.success(request,f"✅ Welcome {username_form}!")
                return redirect('artist_list')
            
    return render(request, 'users/login.html', {'form': LoginForm})

def log_out(request):
    logout(request)
    messages.success(request, '👋 You are now logged out!')
    return redirect('artist_list')

