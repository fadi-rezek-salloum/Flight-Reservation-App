from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Flight(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)

    date = models.DateField()
    time = models.TimeField()

    arrive_date = models.DateField()
    arrive_time = models.TimeField()

    returning_date = models.DateField(null=True, blank=True)
    returning_time = models.TimeField(null=True, blank=True)

    returning_arrive_date = models.DateField(null=True, blank=True)
    returning_arrive_time = models.TimeField(null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    max_passengers = models.PositiveIntegerField(default=100)
    max_weight = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.from_location} -> {self.to_location}"

    def get_absolute_url(self):
        return reverse("flight_detail", kwargs={"pk": self.pk})
    

class FlightReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    number_of_people = models.PositiveIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' -> ' + self.flight.to_location
    
    