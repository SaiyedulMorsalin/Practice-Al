from django.shortcuts import render
from cars.models import CarModel
from brands.models import BrandModel

# def home_page(request):
#     return render(request,'cars_home.html')


try:
    def home_page(request,brand_slug = None):
    
        count = CarModel.objects.all()
        brand_data = CarModel.objects.all()[:4]
        
        if brand_slug is not None:
            brand = BrandModel.objects.get(slug = brand_slug)
            brand_data = CarModel.objects.filter(car_brand=brand)
            count = CarModel.objects.filter(car_brand=brand)
        brands = BrandModel.objects.all()[:9]
        return render(request,'cars_home.html',{'count':count,'brands':brands,'brand_data':brand_data})

except Exception as e:
    print(e)