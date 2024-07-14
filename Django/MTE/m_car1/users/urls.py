from django.urls import path
from .import views
urlpatterns = [
    path('add_user/',views.AddUser.as_view(),name='add_user'),
    path('user_login/',views.UserLogin.as_view(),name='user_login'),
    path('user_logout/',views.LogoutView.as_view(),name='user_logout'),
    # path('user/edit_profile/',views.EditProfile.as_view(),name='edit_user_profile'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile')
]
