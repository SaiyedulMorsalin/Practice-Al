from django.shortcuts import render,redirect
from .forms import SignUpForm
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name,password = userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profile_page')
                
        
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile_page')

def signup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.cleaned_data)
                return redirect('login_page')
                
        else:
            form = SignUpForm()
        return render(request,'sign_up.html',{'form':form})
    else:
        return redirect('login_page')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
        return redirect('login_page')

def userlogout(request):
    logout(request)
    return redirect('login_page')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                return redirect('profile_page')
            
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login_page')