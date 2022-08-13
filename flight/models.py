from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

CATEGORY_CHOICES = [
    ('First Class', 'First Class'),
    ('Economy Class', 'Economy Class')
]

class Category(models.Model):
    name = models.CharField(choices=CATEGORY_CHOICES, max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    

class Flight(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="flights/")

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

    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' -> ' + self.flight.to_location
    
    def save(self, *args, **kwargs):
        if self.flight.returning_date:
            self.total = self.flight.category.price * Decimal(2)
        else:
            self.total = self.flight.category.price

        return super().save(*args, **kwargs)