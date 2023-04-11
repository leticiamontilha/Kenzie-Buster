from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class isUserAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )
    

class IsReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_employee or obj == request.user