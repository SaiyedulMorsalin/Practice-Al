from django.urls import path
from .import views
urlpatterns = [
    path('create_user/',views.create_user,name='create_user'),
    path('user_login/',views.UserLogin.as_view(),name='user_login'),
    path('user_profile/',views.user_profile,name='user_profile'),
]
