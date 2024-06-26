from django.urls import path
from .import views
urlpatterns = [
    path('user_registration/',views.user_registration,name='user_registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
]
