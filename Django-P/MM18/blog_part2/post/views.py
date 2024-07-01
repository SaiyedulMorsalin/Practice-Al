from django.shortcuts import render,redirect
from .forms import PostForm
# Create your views here.
def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('home_page')
    else:
        form = PostForm()
    return render(request,'post.html',{'form':form})