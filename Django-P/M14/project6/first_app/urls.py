from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index_page,name='index_page'),
    path('home/',views.home,name='home'),
    path('delete/<int:roll>',views.delete_student,name='delete_student'),
]
