from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    path('contact-us/', views.contact),
    
    path('flight/<str:destination>/', views.flightDestination),
    path('flight/<pk>/detail/', views.flightDetail, name='flight_detail'),
    path('flight/<pk>/reserve/', views.flightReserve, name='flight_reserve'),
    path('flight/not-found/', views.flight_404),
]
