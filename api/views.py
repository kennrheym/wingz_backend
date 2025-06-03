from api.models import User, Ride, RideEvent
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, RideSerializer, RideEventSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from api.permissions import IsAdminRole
from api.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import RideFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['pickup_time']  # Customize based on your model
    # ordering = ['-pickup_time']  # Default ordering
    
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['pickup_time']  # Customize based on your model
    ordering = ['-pickup_time']  # Default ordering
    filterset_class = RideFilter

class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['pickup_time']  # Customize based on your model
    # ordering = ['-pickup_time']  # Default ordering