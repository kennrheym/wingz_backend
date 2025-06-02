from rest_framework import serializers
from .models import User, Ride, RideEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role']


class RideSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer(read_only=True)
    id_driver = UserSerializer(read_only=True)

    class Meta:
        model = Ride
        fields = [
            'id',
            'status',
            'id_rider',
            'id_driver',
            'pickup_latitude',
            'pickup_longitude',
            'dropoff_latitude',
            'dropoff_longitude',
            'pickup_time'
        ]


class RideEventSerializer(serializers.ModelSerializer):
    id_ride = RideSerializer(read_only=True)

    class Meta:
        model = RideEvent
        fields = ['id', 'id_ride', 'description', 'created_at']
