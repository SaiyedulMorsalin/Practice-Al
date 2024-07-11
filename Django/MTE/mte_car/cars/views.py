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
        pk_url_kwarg = 'id'
        template_name = 'car_detail.html'
        context_object_name = 'car'
    
    def comment(request):
        form = CommentForm()
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,'new_cars.html',{'form':form})
    
except Exception as e:
    print(e)