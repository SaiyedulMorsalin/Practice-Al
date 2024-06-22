from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # print(data)
            form.save()
            return redirect('home_page')
    else:
        form = RegisterForm()
    return render(request,'register_login.html',{'form':form,'type':'Register'})




def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_password)
            if user is not None:
                login(request,user)
                return redirect('home_page')
                
    else:
        form = AuthenticationForm()            
    return render(request,'register_login.html',{'form':form,'type':'Login'})
        
def user_logout(request):
    logout(request)
    return redirect('home_page')
