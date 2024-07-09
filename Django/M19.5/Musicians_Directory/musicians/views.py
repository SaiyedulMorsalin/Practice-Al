from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import MusicianModel
from .forms import MusicianForm,UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import RedirectView
from django.contrib.auth import logout
# Create your views here.
class AddMusician(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = './form.html'
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class AddUser(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = './register.html'
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EditUser(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = './form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')
    
class UserLogin(LoginView):
    template_name = './login.html'
    def get_success_url(self):
        return reverse_lazy('home_page')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    

class LogoutView(RedirectView):
    url = '/user_login'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)