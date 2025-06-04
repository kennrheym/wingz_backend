from rest_framework import serializers
from .models import User, Ride, RideEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class RideEventSerializer(serializers.ModelSerializer):
    # id_ride = RideSerializer(read_only=True)

    class Meta:
        model = RideEvent
        fields = ['id', 'id_ride', 'description', 'created_at']

class RideSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer(read_only=True)
    id_driver = UserSerializer(read_only=True)
    ride_events = RideEventSerializer(source='rideevent_set', many=True, read_only=True)

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
            'pickup_time',
            'ride_events'
        ]



