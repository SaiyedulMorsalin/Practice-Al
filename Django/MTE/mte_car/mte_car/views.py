from django.shortcuts import render
from cars.models import AddCarModel
# Create your views here.
def home_page(request):
    data = AddCarModel.objects.all()[:4]
    count = AddCarModel.objects.all()
    
    return render(request,'index.html',{'data':data,'count':count})