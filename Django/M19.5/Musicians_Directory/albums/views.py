from django.shortcuts import render
from .forms import AlbumForm
from .models import AlbumModel
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class AddAlbum(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = './album_form.html'
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    

class IndexPage(DetailView):
    model = AlbumModel
    template_name = 'index.html'

class EditAlbum(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = './album_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')

class DeleteAlbum(DeleteView):
    model = AlbumModel
    template_name = './delete.html'
    success_url = reverse_lazy('home_page')
    pk_url_kwarg = 'id'

    
