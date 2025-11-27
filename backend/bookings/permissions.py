from rest_framework.permissions import BasePermission

class IsBookingOwnerOrBusinessStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # customer can only view their own
        if request.user == obj.customer:
            return True
        
        # business owner or staff can access booking
        if hasattr(obj.business, "owner") and obj.business.owner == request.user:
            return True
        
        return False