from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request,'index.html')

def user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Account Created Successfully !! Please Login')
            return redirect('user_login')
        
    else:
        form = SignUpForm()
    return render(request,'registration.html',{'form':form})

def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password= password)
            if user is not None:
                login(request=request,user=user)
                messages.success(request,'Logged In Successfully')
                return redirect('user_profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('user_login')


def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('user_login')

def user_change_pass(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('user_profile')
    else:
        form = SetPasswordForm(request.POST)
    return render(request,'password_change.html',{'form':form})
            
