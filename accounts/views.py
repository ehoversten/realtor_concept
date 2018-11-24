from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        messages.error(request, "Testing error message")
        # REGISTER USER
        print('POST SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # LOGIN USER
        print('POST SUBMITTED LOGIN')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
