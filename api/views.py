from api.models import User, Ride, RideEvent
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, RideSerializer, RideEventSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class RideViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving rides.
    """
    def list(self, request):
        queryset = Ride.objects.all()
        serializer = RideSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Ride.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RideSerializer(user)
        return Response(serializer.data)

class RideEventViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving ride events.
    """
    def list(self, request):
        queryset = RideEvent.objects.all()
        serializer = RideEventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = RideEvent.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RideEventSerializer(user)
        return Response(serializer.data)