from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.userlogin,name='login_page'),
    path('signup/',views.signup,name='signup_page'),
    path('profiles/',views.profile,name='profile_page'),
    path('logout/',views.userlogout,name='logout_page'),
    path('pass_change/',views.pass_change,name='pass_change'),
]
