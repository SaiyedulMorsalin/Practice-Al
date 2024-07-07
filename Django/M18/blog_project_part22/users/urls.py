from django.urls import path
from .import views
urlpatterns = [
    path('user_create/',views.user_create,name='user_create'),
    path('user_profile_edit/',views.user_profile_edit,name='user_profile_edit'),
    path('user_profile_edit/change_pass/',views.user_profile_change_pass,name='user_profile_change_pass'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
