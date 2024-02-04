from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from newtest.forms import LoginForm
from django.contrib import messages


def submit(request):
    return render(request,'index.html')

def submit1(request):
    return render(request,'index.html')

def cal(request):
    return render (request,'calculator.html')

