from django.shortcuts import render
from post.models import PostModel
def home_page(request):
    data = PostModel.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})



