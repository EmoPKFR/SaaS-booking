from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import WorkingHours
from .serializers import WorkingHoursSerializer
from .permissions import IsBusinessOwner
from businesses.models import Business


class WorkingHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticatedOrReadOnly(), IsBusinessOwner()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        business_id = self.request.data.get("business_id")
        if not business_id:
            raise ValueError("business_id is required.")

        business = Business.objects.get(id=business_id)

        # Ensure current user is owner
        if business.owner != self.request.user:
            raise PermissionError("You cannot modify another owner's schedule.")

        serializer.save(business=business)
