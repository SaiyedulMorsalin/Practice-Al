from django.urls import path
from .import views
urlpatterns = [
    path('',views.index_page,name='index_page'),
    path('signup/',views.user_registration,name='user_signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.user_profile,name='user_profile'),
    path('profile/password_change',views.user_change_pass,name='user_change_pass'),
]
