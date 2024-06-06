from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about_page'),
    path('html_form/',views.html_form,name='html_form'),
    path('django_form/',views.django_form,name='django_form'),
]
