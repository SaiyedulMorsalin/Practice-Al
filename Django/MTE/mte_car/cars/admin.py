from django.contrib import admin
from .models import AddCarModel,CommentModel,UserOrder
# Register your models here.
admin.site.register(AddCarModel)
admin.site.register(CommentModel)
admin.site.register(UserOrder)
