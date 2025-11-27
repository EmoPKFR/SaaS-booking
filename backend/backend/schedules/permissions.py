from rest_framework.permissions import BasePermission
from businesses.models import Business


class IsBusinessOwner(BasePermission):

    def has_permission(self, request, view):
        # Create, update, delete require authentication
        if view.action in ["create", "update", "partial_update", "destroy"]:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        # obj is a WorkingHours instance
        return obj.business.owner == request.user
