from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        # check for delete user by him/herself
        if obj.username == request.user.username:
            return True
        return False
