from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index_home'),
    path('form/',views.form_page,name='form_page'),
]
