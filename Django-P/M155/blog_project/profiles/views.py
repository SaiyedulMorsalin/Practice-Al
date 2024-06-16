from django.shortcuts import render
from .forms import ProfilesForm
# Create your views here.
def add_profiles(request):
    form = ProfilesForm()
    return render(request,'./add_profiles.html',{'form':form})