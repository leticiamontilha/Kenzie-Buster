from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsAdminOrReadOnLy(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )
    

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        if user == request.user or request.user.is_employee:
            return True
        
        return False