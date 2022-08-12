from django.contrib import admin

from .models import Car, CarReservation

admin.site.register(CarReservation)
admin.site.register(Car)