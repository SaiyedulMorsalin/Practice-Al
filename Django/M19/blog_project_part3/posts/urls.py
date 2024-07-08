from django.urls import path
from .import views 
urlpatterns = [
    # path('create/',views.post_create,name='post_create'),
    path('create/',views.PostCreate.as_view(),name='post_create'),
    # path('edit/<int:id>/',views.post_edit,name='post_edit'),
    path('edit/<int:id>/',views.PostEdit.as_view(),name='post_edit'),
    # path('delete/<int:id>/',views.post_delete,name='post_delete'),
    path('delete/<int:id>/',views.PostDeleteView.as_view(),name='post_delete'),
    
]
