from rest_framework.permissions import BasePermission
from rest_framework import status

from users.models import User


class IsCreator(BasePermission):
    """
    This permission checks whether the request user is owner of the instance or not.
    """
    message = "Only creator has permission to perform this action."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user