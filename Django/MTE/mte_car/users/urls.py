from django.urls import path
from . import views

urlpatterns = [
    path('add_user/',views.AddUser.as_view(),name='add_user'),
    path('user_login/',views.UserLogin.as_view(),name='user_login'),
    path('user_logout/',views.LogoutView.as_view(),name='user_logout'),
]
