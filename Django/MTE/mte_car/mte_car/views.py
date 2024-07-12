from django.shortcuts import render
from cars.models import AddCarModel
from brands.models import BrandModel
# Create your views here.
try:
    def home_page(request,brand_slug = None):
    
        count = AddCarModel.objects.all()
        brand_data = AddCarModel.objects.all()[:4]
        
        if brand_slug is not None:
            brand = BrandModel.objects.get(slug = brand_slug)
            brand_data = AddCarModel.objects.filter(car_brand=brand)
            count = AddCarModel.objects.filter(car_brand=brand)
        brands = BrandModel.objects.all()
        return render(request,'index.html',{'count':count,'brands':brands,'brand_data':brand_data})

except Exception as e:
    print(e)