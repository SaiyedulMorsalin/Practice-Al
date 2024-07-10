from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm
from .models import PostModel
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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
@method_decorator(login_required,name='dispatch')
class PostCreate(CreateView):
    model = PostModel
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('user_profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class PostEdit(UpdateView):
    model = PostModel
    form_class = PostForm
    template_name =  'post_create.html'
    success_url = reverse_lazy('user_profile')
    pk_url_kwarg = 'id'
    
    

class PostDeleteView(DeleteView):
    model = PostModel
    
    pk_url_kwarg = 'id'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('user_profile')
    

class PostDetailView(DetailView):
    model = PostModel
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return self.get(request,*args,**kwargs)
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.object # post modeler object store krlam 
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        
    
    
    
    
    
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

