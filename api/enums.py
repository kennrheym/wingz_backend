from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'Admin'
    DRIVER = 'Driver'
    RIDER = 'Rider'


class RideStatus(models.TextChoices):
    EN_ROUTE = 'EnRoute'
    PICKED_UP = 'PickedUp'
    DROPPED_OFF = 'DroppedOff'