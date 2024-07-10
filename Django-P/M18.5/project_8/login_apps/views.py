from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home_page(request):
    return render(request,'index.html')
def login_page(request):
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})