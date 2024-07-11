from django.urls import path
from .import views
urlpatterns = [
    path('show_all_cars/',views.show_more,name='show_all_cars'),
    path('car_details/<int:id>/',views.CarDetail.as_view(),name='car_detail'),
]
