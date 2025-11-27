from rest_framework.permissions import BasePermission


class IsBusinessOwner(BasePermission):
    """
    Allow only users with role=owner to create a business.
    Also allow editing only if the business belongs to the user.
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated and request.user.role == 'owner'
        return True
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user