from django.urls import path
from .import views

urlpatterns = [
    path('user_create/',views.user_create,name='user_create'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_profile/edit/',views.user_profile_edit,name='user_profile_edit'),
    path('user/profile/pass_change/',views.user_pass_change,name='user_pass_change'),
    
]
