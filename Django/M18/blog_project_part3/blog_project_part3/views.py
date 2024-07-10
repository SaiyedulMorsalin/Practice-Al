from django.shortcuts import render
from posts.models import PostModel
from categories.models import Category
def home_page(request,category_slug = None):
    data = PostModel.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = PostModel.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request,'index.html',{'data':data,'category':categories})