from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return bool(
            request.user.is_authenticated
            and request.user.is_admin
            or obj.author == request.user
        )
