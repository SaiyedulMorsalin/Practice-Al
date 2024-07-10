from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.user_signup,name='signup_page'),
    path('login/',views.user_login,name='login_page'),
    path('profile/',views.user_profile,name='profile_page'),
    path('logout/',views.user_logout,name='logout_page'),
]
