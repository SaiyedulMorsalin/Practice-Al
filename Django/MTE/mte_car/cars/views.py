from django.shortcuts import render
from .models import AddCarModel,CommentModel
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .forms import CommentForm
# Create your views here.

try:
    class ShowMore(ListView):
        model = AddCarModel
        template_name = 'cars.html'
        context_object_name = 'data'

    class CarDetail(DetailView):
        model = AddCarModel
        form_class = CommentForm
        pk_url_kwarg = 'id'
        template_name = 'car_detail.html'
        context_object_name = 'car'
        def post(self, request, *args, **kwargs):
            comment_form = CommentForm(data=self.request.POST)
            car = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
            return self.get(request, *args, **kwargs)
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            car = self.object # post model er object ekhane store korlam
            comments = car.comments.all()
            comment_form = CommentForm()
            
            context['comments'] = comments
            context['comment_form'] = comment_form
            return context
        
        
    
    
    
except Exception as e:
    print(e)