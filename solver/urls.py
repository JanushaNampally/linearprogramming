from django.urls import path 
from . import views 
from .views import simplex_method

urlpatterns = [
    path('', views.home, name='home'),
    path('simplex/', simplex_method, name='simplex'),
    path('graphical/', views.graphical_method, name='graphical'),
    path('transportation/', views.transportation_method, name='transportation'),
    
]
