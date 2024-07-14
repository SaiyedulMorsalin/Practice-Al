from django.shortcuts import render
from cars.models import CarModel
from brands.models import BrandModel
from orders.models import UserOrder
# def home_page(request):
#     return render(request,'cars_home.html')


try:
    def home_page(request,brand_slug = None):
    
        count = CarModel.objects.all()
        brand_data = CarModel.objects.all()[:6]
        if brand_slug is not None:
            brand = BrandModel.objects.get(slug = brand_slug)
            brand_data = CarModel.objects.filter(car_brand=brand)
            count = CarModel.objects.filter(car_brand=brand)
        brands = BrandModel.objects.all()[:9]
    
        total_quantity = sum(car.car_stock_quantity for car in count)
        print(total_quantity)
        return render(request,'cars_home.html',{'count':total_quantity,'brands':brands,'brand_data':brand_data})

except Exception as e:
    print(e)