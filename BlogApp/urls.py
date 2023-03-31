from django.urls import path 
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('dashboard/',views.DashBoard, name='dashboard'),
    path('addblog/',views.addblog, name='addblog'),
    path('deleteblog/<int:id>/',views.deleteblog, name='deleteblog'),
    path('updateblog/<int:id>/',views.updateblog, name='updateblog'),
    
]