from django.shortcuts import render,redirect
from .forms import PostForm
from .models import PostModel
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home_page')
    else:
        form = PostForm()
        return render(request,'./add_post.html',{'form':form})
    
    
def edit_post(request,id):
    post = PostModel.objects.get(pk = id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request,'./add_post.html',{'form':form})


def delete_post(request,id):
    post = PostModel.objects.get(pk=id)
    post.delete()
    return redirect('home_page')
    
    
    