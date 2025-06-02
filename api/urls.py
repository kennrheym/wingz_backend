from django.urls import path, include
# from .views import BookListCreateAPIView, BookDetailAPIView
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, RideViewSet, RideViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'rides', RideViewSet, basename='ride')
router.register(r'ride_events', RideViewSet, basename='ride_event')

urlpatterns = [
    path('', include(router.urls)),
]