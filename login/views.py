from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.

def ShowLogin(request):
    return render(request,'login/index.html')

def MakeRegistration(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    User.objects.create_user(username,email,password)
    return redirect("/")

def Login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/homepage/")
    else:
        return redirect("/")
