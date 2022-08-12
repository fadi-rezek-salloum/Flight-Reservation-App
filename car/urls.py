from django.urls import path

from . import views

urlpatterns = [
    path('', views.carsHome),
    path('cars-list/<str:location>/', views.carsList),
    path('cars-list/', views.carsList),
    path('detail/<pk>/', views.carDetail),
    path('reserve/<pk>/', views.carReserve),
]
