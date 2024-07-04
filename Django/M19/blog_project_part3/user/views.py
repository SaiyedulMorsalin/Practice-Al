from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def create_user(request):
    form = UserCreateForm()
    return render(request,'registration.html',{'form':form})


def login_user(request):
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_profile(request):
    return render(request,'profile.html')


class UserLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('user_profile')
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form = form))