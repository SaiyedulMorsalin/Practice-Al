from django.shortcuts import render
from .forms import AuthorForm
# Create your views here.
def add_author(request):
    form = AuthorForm()
    
    return render(request,'./add_author.html',{'form':form})
