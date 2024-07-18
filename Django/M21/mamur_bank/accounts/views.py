from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login 
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class UserLogin(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home_page')
    
class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        
        return reverse_lazy('home_page')
    