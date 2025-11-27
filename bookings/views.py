from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsBookingOwnerOrBusinessStaff

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "owner":
            return Booking.objects.filter(business__owner=user)
        elif user.role == "staff":
            return Booking.objects.filter(business__staff=user)
        else:
            return Booking.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
