from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotelsHome),
    path('hotels-list/<str:destination>/', views.hotelsList),
    path('hotels-list/', views.hotelsList),
    path('detail/<pk>/', views.hotelDetail),
    path('reserve/<pk>/', views.roomReserve),
]