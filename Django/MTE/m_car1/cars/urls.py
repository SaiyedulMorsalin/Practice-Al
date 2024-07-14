from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from .import views
urlpatterns = [
    path('show_all_cars/',views.ShowMore.as_view(),name='show_all_cars'),
    path('add_car/',user_passes_test(lambda u: u.is_superuser)(views.AddCar.as_view()),name='add_car'),
    path('car_details/<int:id>/',views.CarDetail.as_view(),name='car_detail'),
]
