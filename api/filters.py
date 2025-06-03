# api/filters.py
import django_filters
from api.models import Ride

class RideFilter(django_filters.FilterSet):
    rider_email = django_filters.CharFilter(field_name='id_rider__email', lookup_expr='iexact')

    class Meta:
        model = Ride
        fields = ['status', 'rider_email']
