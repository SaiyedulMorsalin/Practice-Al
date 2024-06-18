from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from .views import profile

urlpatterns = [
    path('profile/',profile,name='profile'),
]