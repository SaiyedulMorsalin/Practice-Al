from django.urls import path
from .import views
urlpatterns = [
    path('show_all_cars/',views.ShowMore.as_view(),name='show_all_cars'),
    path('car_details/<int:id>/',views.CarDetail.as_view(),name='car_detail'),
    path('car/<int:car_id>/buy_now/',views.buy_now,name='buy_now'),
    path('order/<int:order_id>/confirmation/',views.order_confirmation,name='order_con'),

]
