from django.urls import path
from .import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('user_login/',views.login_page,name='user_login')
]
