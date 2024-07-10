from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
import time
# Create your views here.

def user_signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            messages.success(request,"Account Created Successfully.")
        
        # return redirect('home_page')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            messages.success(request,"Account Login Successfully.")
            # messages.error(request,"Please Enter a Correct username and Password.")
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_password)
            if user:
                login(request,user)
                t = 2
                time.sleep(t)
    
        # return redirect('profile_page')
    else:
        form = AuthenticationForm(request,request.POST)
    return render(request,'login.html',{'form':form})


def user_profile(request):
    return render(request,'profiles.html')

def user_logout(request):
    
    logout(request)
    return redirect('home_page')
    