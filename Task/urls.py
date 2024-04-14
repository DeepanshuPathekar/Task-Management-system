from django.contrib import admin 
from django.urls import path
from .import views



urlpatterns = [
path('admin/', admin.site.urls),
path('',views.home,name='home'),
path('user_list',views.user_list,name='user_list'),
path('export_data',views.export_data,name='export_data'),
]