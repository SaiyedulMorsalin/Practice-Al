from django.shortcuts import render,redirect
from .froms import UserCreatingForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from posts.models import PostModel
from .froms import UserChangingForm
# Create your views here.






def user_create(request):
    if request.method =='POST':
        form  = UserCreatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreatingForm()
    return render(request,'user_create.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                login(request,user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request,'user_login.html',{'form':form})
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
    
@login_required
def user_profile(request):
    data = PostModel.objects.filter(user = request.user)
    return render(request,'user_profile.html',{'data':data})


@login_required
def user_profile_edit(request):
    if request.method == 'POST':
        form = UserChangingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        
    else:
        form = UserChangingForm(instance=request.user)
    return render(request,'user_profile_edit.html',{'form':form})


@login_required
def user_pass_change(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,data = request.POST)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'user_change_pass.html',{'form':form})
        
        

