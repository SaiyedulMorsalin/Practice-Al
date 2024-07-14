from django.shortcuts import render,get_object_or_404,redirect
from .models import UserOrder
from cars.models import CarModel
# Create your views here.
try:
    pass
    def buy_now(request,car_id):
            car = get_object_or_404(CarModel,id = car_id)
            if car.car_stock_quantity >0:
                order = UserOrder.objects.create(
                    user = request.user,
                    car = car,
                    quantity = 1,
                    total_price = car.car_price
                )
                car.car_stock_quantity -=1
                car.save()
                return redirect('order_conf',order_id = order.id)
            else:
                return redirect('car_detail',car_id = car.id)
            
        
    def order_confirmation(request,order_id):
        order = get_object_or_404(UserOrder,id = order_id,user = request.user)
        return render(request,'order_conf.html',{'order':order})
except Exception as e:
    print(e)