from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('cars/', views.CarsList.as_view(), name='cars_list'),
    path('cars/new/', views.CarCreate.as_view(), name='car_create'),
]