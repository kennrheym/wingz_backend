from rest_framework import serializers
from .models import User, Ride, RideEvent
from geopy.distance import geodesic
from .enums import RideStatus
from datetime import date

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
    class Meta:
        model = RideEvent
        fields = ['id', 'id_ride', 'description', 'created_at']


class RideSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer(read_only=True)
    id_driver = UserSerializer(read_only=True)
    distance = serializers.SerializerMethodField()

    # ride_events = RideEventSerializer(source='rideevent_set', many=True, read_only=True)
    todays_ride_events = RideEventSerializer(source='rideevent_set', many=True, read_only=True)
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
            # 'ride_events',
            'distance',
            'todays_ride_events'
        ]
    
    def get_distance(self, obj):
        driver_lat = self.context.get('driver_latitude')
        driver_long = self.context.get('driver_longitude')
        if driver_lat and driver_long and obj.status == RideStatus.EN_ROUTE:
            try:
                coord1 = (float(driver_lat), float(driver_long))
                coord2 = (obj.pickup_latitude, obj.pickup_longitude)
                return round(geodesic(coord1, coord2).kilometers, 2)
            except Exception:
                return None
        return None
    
    def get_todays_ride_events(self, obj):
        today = date.today()
        todays_events = obj.rideevent_set.filter(created_at__date=today)
        return RideEventSerializer(todays_events, many=True).data



