from django.urls import path,include
from . import views
urlpatterns = [
    path('add_profile/',views.add_profiles,name='add_profile'),
]