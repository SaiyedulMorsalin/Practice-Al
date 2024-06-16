from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def add_post(request):
    form = PostForm()
    return render(request,'./add_post.html',{'form':form})