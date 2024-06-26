from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangerUserForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # print(data)
            form.save()
            return redirect('user_profile')
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
                return redirect('user_profile')
                
    else:
        form = AuthenticationForm()            
    return render(request,'register_login.html',{'form':form,'type':'Login'})
@login_required     
def user_logout(request):
    logout(request)
    return redirect('home_page')

@login_required
def user_profile(request):
        return render(request, 'profile.html', { 'type': 'Profile'}) 


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = ChangerUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            print(data)
            return redirect('user_profile')
    else:
        form = ChangerUserForm(instance=request.user)
    return render(request, 'profile.html', {'form': form, 'type': 'Profile Edit'})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pc.html', {'form': form, 'type': 'Password Change'})