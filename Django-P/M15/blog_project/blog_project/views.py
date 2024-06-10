from django.shortcuts import render
from post.models import Post

def home_page(request):
    data = Post.objects.all()
    # print(data)
    return render(request,'home.html',{'data':data})