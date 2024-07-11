from django.shortcuts import render
from cars.models import AddCarModel
# Create your views here.
try:
    def home_page(request):
        data = AddCarModel.objects.all()[:4]
        count = AddCarModel.objects.all()
        return render(request,'index.html',{'data':data,'count':count})

except Exception as e:
    print(e)