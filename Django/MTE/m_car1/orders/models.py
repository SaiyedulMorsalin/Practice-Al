from django.db import models
from cars.models import CarModel
from django.contrib.auth.models import User
# Create your models here.
class UserOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price =models.DecimalField(max_digits=10,decimal_places=2)
    order_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id}"