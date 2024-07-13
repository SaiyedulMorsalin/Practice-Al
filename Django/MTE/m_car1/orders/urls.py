from django.urls import path
from .import views
urlpatterns = [
    path('car/<int:car_id>/buy_now/',views.buy_now,name='buy_now'),
    path('order/<int:order_id>/confirmation/',views.order_confirmation,name='order_conf'),
]
