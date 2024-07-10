from django.shortcuts import render
from .forms import UserCreateForm
# Create your views here.

def user_create(request):
    form = UserCreateForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    return None

def user_logout(request):
    pass

def user_profile(request):
    pass
