from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

import re


# Create your views here.

def ShowLogin(request):
    return render(request,'login/index.html')

def MakeRegistration(request):
    username = request.POST["username"]
    email = request.POST["email"]
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(email):
        return HttpResponse("Enter a valid email")
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is None:
        User.objects.create_user(username,email,password)
        return redirect("/")
    else:
        return HttpResponse("Please try again")
    

def Login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/homepage/")
    else:
        return redirect("/")
