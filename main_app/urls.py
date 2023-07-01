from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('cars/', views.CarsList.as_view(), name='cars_list'),
    path('cars/new/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name="car_update"),
]