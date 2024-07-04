from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .forms import PostForm
from .models import PostModel
from django.urls import reverse_lazy
def add_post(request):
    
    
    form = PostForm()
    return render(request,'add_post.html',{'form':form})


class AddPost(CreateView):
    model = PostModel
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


