from django.contrib import admin
from .models import Category, Flight, FlightReservation

admin.site.register(Category)
admin.site.register(Flight)
admin.site.register(FlightReservation)