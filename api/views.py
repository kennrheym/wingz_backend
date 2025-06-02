from api.models import User, Ride, RideEvent
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, RideSerializer, RideEventSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from api.permissions import IsAdminRole

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdminRole]
    
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes=[IsAdminRole]

class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes=[IsAdminRole]