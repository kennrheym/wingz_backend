from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import UserRole, RideStatus

# Create your models here.
class User(AbstractUser):
    role = models.CharField(
        choices=UserRole.choices,
    )
    phone_number = models.CharField(max_length=25, unique=True)

class Ride(models.Model):
    status = models.CharField(
        choices=RideStatus.choices,
    )
    id_rider = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="id_rider"
    )
    id_driver = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="id_driver"
    )
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

class RideEvent(models.Model):
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
