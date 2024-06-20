from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    form = SignUpForm()
    return render(request,'sign_up.html',{'form':form})

def profile(request):
    return render(request,'profile.html')