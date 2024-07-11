from django.shortcuts import render
from .models import AddCarModel
from django.views.generic import DetailView
# Create your views here.


def show_more(request):
    data = AddCarModel.objects.all()
    return render(request,'cars.html',{'data':data})

class CarDetail(DetailView):
    model = AddCarModel
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'
    
    