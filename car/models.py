from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()

    pick_up_time = models.TimeField()
    drop_off_time = models.TimeField()
     
    price_per_day = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    auto_gear = models.BooleanField()
    number_of_people = models.PositiveIntegerField(default=4)

    def __str__(self):
        return self.car_name
     

class CarReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    from_date = models.DateField(auto_now_add=True)
    from_time = models.TimeField(auto_now_add=True)

    number_of_days = models.PositiveIntegerField(default=1)

    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username + ' -> ' + self.car.car_name

    def save(self, *args, **kwargs):
        self.total = self.number_of_days * self.car.price_per_day

        return super().save(*args, **kwargs)    