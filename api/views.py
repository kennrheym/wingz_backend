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
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['pickup_time']  # Customize based on your model
    # ordering = ['-pickup_time']  # Default ordering
    
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
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     driver_latitude = self.request.query_params.get('driver_latitude')
    #     driver_longitude = self.request.query_params.get('driver_longitude')
    #     order_by_distance = self.request.query_params.get('ordering') == 'distance'

    #     if order_by_distance and driver_latitude and driver_longitude:
    #         driver_coord = (float(driver_latitude), float(driver_longitude))

    #         # Convert to list to annotate and sort
    #         queryset = list(queryset)
    #         for ride in queryset:
    #             ride.distance = geodesic(
    #                 driver_coord,
    #                 (ride.pickup_latitude, ride.pickup_longitude)
    #             ).kilometers

    #         queryset.sort(key=lambda r: r.distance)

    #     return queryset
    
    # def paginate_queryset(self, queryset):
    #     if isinstance(queryset, list):
    #         paginator = self.pagination_class()
    #         page_size = paginator.get_page_size(self.request)
    #         if not page_size:
    #             return None

    #         page_number = self.request.query_params.get(paginator.page_query_param, 1)
    #         try:
    #             page_number = int(page_number)
    #         except ValueError:
    #             page_number = 1

    #         start = (page_number - 1) * page_size
    #         end = start + page_size
    #         paginated_list = queryset[start:end]

    #         # Store pagination info for response
    #         self._paginator = paginator
    #         self._paginator.page = page_number
    #         self._paginator.count = len(queryset)
    #         self._paginator.num_pages = (len(queryset) + page_size - 1) // page_size

    #         return paginated_list
    #     else:
    #         return super().paginate_queryset(queryset)



class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes=[IsAdminRole]
    pagination_class = DefaultPagination
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['pickup_time']  # Customize based on your model
    # ordering = ['-pickup_time']  # Default ordering