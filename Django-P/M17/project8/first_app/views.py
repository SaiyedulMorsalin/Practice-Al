from django.shortcuts import render
from .forms import LoginForm,SignupForm
# Create your views here.
def login(request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def sign_up(request):
    form = SignupForm()
    return render(request,'sign_up.html',{'form':form})