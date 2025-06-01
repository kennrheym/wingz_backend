from django.db import models
from .enums import UserRole, RideStatus

# Create your models here.
class User(models.Model):
    role = models.CharField(
        choices=UserRole.choices,
    )
    first_name = models.TextField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()

class Ride(models.Model):
    status = models.CharField(
        choices=RideStatus.choices,
    )
    id_rider = models.ForeignKey(User, on_delete=models.CASCADE)
    id_driver = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

class RideEvent(models.Model):
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
