
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page,name= 'index_page'),
    path('',include('user.urls')),
    path('',include('post.urls'))
]
