from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        new_user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
    context = {
        'errors': new_user[1]
        }
    return render(request, 'login/index.html', context)

def login(request):
    if request.method == 'POST':
         user = User.userManager.login(request.POST['email'], request.POST['password'])
    return render(request, 'login/success.html')
