from django.urls import path

from first_app.views import index


urlpatterns = [
    path('',index,name='index'),
]
