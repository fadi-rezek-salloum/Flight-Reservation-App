from django.contrib import admin

from .models import Hotel, HotelReservation

admin.site.register(HotelReservation)
admin.site.register(Hotel)