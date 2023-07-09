#from django.shortcuts import render
from django.shortcuts import render


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')