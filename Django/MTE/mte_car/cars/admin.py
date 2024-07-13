from django.contrib import admin
from .models import CarModel,CommentModel
from orders.models import UserOrder
# Register your models here.
admin.site.register(CarModel)
admin.site.register(CommentModel)
admin.site.register(UserOrder)
