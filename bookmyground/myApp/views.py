from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def loginUser(request):
    return render(request, 'login.html')


def signupUser(request):
    return render(request, 'signup.html')
