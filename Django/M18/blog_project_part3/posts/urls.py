from django.urls import path
from .import views 
urlpatterns = [
    path('create/',views.post_create,name='post_create'),
    path('edit/<int:id>/',views.post_edit,name='post_edit'),
    path('delete/<int:id>/',views.post_delete,name='post_delete'),
    
]
