from api.models import User, Ride, RideEvent
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, RideSerializer, RideEventSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from api.permissions import IsAdminRole
from api.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import RideFilter
from .enums import RideStatus
from geopy.distance import geodesic


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    # filter_backends = [DjangoFilterBackend]
    ordering_fields = ['pickup_time']
    ordering = ['-pickup_time']
    filterset_class = RideFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['driver_latitude'] = self.request.query_params.get('driver_latitude')
        context['driver_longitude'] = self.request.query_params.get('driver_longitude')
        return context

class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination