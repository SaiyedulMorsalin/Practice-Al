from django.urls import path
from .import views
urlpatterns = [
    path('add_musician/',views.AddMusician.as_view(),name='add_musician'),
    path('add_user/',views.AddUser.as_view(),name='add_user'),
    path('user_login/',views.UserLogin.as_view(),name='user_login'),
    path('edit_user/<int:id>',views.EditUser.as_view(),name='edit_user'),
    path('user_logout/',views.LogoutView.as_view(),name='user_logout'),
]
