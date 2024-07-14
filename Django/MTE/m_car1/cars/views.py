from django.shortcuts import render,redirect
from .models import CarModel
from django.views.generic import DetailView,CreateView
from django.views.generic.list import ListView
from .forms import CommentForm,AddCarForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

try:
    class ShowMore(ListView):
        model = CarModel
        template_name = 'car_all_show.html'
        context_object_name = 'data'
        
        
    @method_decorator(login_required,name='dispatch')
    class AddCar(CreateView):
        model = CarModel
        form_class = AddCarForm
        template_name = 'add_car.html'
        success_url = reverse_lazy('home_page')
        def form_valid(self, form):
            form.save()
            return super().form_valid(form)
    class CarDetail(DetailView):
        model = CarModel
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
            car = self.object # addcar  model er object ekhane store korlam
            comments = car.comments.all()
            comment_form = CommentForm()
            context['comments'] = comments
            context['comment_form'] = comment_form
            return context
        
    
except Exception as e:
    print(e)