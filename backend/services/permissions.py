from rest_framework.permissions import BasePermission


class IsBusinessOwnerOfService(BasePermission):
     """
    Allow only the owner of the business to manage its services.
    """
     
     def has_object_permission(self, request, view, obj):
          return obj.business.owner == request.user