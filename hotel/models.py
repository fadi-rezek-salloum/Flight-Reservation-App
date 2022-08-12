from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    going_to = models.CharField(max_length=50)
    pool = models.BooleanField(default=False)
    breakfast_included = models.BooleanField(default=False)
    free_airport_shuttle = models.BooleanField(default=False)
    business_services = models.BooleanField(default=False)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_people = models.PositiveIntegerField(default=1)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    ac_tv = models.BooleanField()
    image = models.ImageField(upload_to='rooms/')
    image2 = models.ImageField(upload_to='rooms/')
    image3 = models.ImageField(upload_to='rooms/')
    image4 = models.ImageField(upload_to='rooms/')
    image5 = models.ImageField(upload_to='rooms/')
    price_per_24_h = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    if_free = models.BooleanField(default=True)

    def __str__(self):
        return f"Room for {self.number_of_people} people"
     

class HotelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    from_date = models.DateTimeField(auto_now_add=True)

    number_of_days = models.PositiveIntegerField(default=1)

    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username + ' -> ' + str(self.hotel.id)

    def save(self, *args, **kwargs):
        self.total = Decimal(self.number_of_days) * self.hotel.price_per_24_h

        return super().save(*args, **kwargs)
    