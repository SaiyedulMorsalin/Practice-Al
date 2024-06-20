from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.login,name='login_page'),
    path('signup/',views.signup,name='signup_page'),
    path('profiles/',views.profile,name='profile_page'),
]
