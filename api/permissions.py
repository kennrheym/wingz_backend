from rest_framework.permissions import BasePermission
from api.enums import UserRole

class IsAdminRole(BasePermission):
    """
    Allows access only to users with role 'Admin'.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser or (request.user.is_authenticated and getattr(request.user, 'role', None) == UserRole.ADMIN)