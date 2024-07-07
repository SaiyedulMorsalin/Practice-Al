from django.shortcuts import render,redirect
from .forms import UserCreatingForm,UserChangingForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def user_create(request):
    if request.method =='POST':
        form = UserCreatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        
    form = UserCreatingForm()
    return render(request,'user_create.html',{'form':form})

def user_profile_edit(request):
    form = UserChangingForm()
    return render(request,'user_profile_edit.html',{'form':form})

def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data =request.POST)
        if form.is_valid():
            
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(request,username=user_name,password = user_pass)
            if user is not None:
                login(request,user)
                return redirect('user_profile')
    
    else:  
        form = AuthenticationForm()
    return render(request,'user_login.html',{'form':form})

def user_profile(request):
    return render(request,'user_profile.html')

def user_profile_change_pass(request):
    form = SetPasswordForm(request.user)
    return render(request,'user_pass_change.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('user_login')