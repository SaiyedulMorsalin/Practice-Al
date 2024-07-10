from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import PostModel
# Create your views here.

@login_required
def post_create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('post_create')
    else:
        form = PostForm()
    return render(request,'./post_create.html',{'form':form})

    

def post_edit(request,id):
    post = PostModel.objects.get(pk = id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('user_profile')
    
    return render(request,'post_create.html',{'form':form})
def post_delete(request,id):
    post = PostModel.objects.get(pk = id)
    post.delete()
    return redirect('home_page')

