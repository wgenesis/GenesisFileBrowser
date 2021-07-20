from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')

def logout(request):
    return redirect('/login/')