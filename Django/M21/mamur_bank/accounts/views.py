from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login 
from django.views.generic import FormView
from .forms import UserRegistrationForm
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    