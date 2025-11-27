from rest_framework import serializers
from .models import Booking
from datetime import timedelta

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "business",
            "service",
            "customer",
            "start_time",
            "end_time",
            "status",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ("customer", "end_time", "status")

    def validate(self, data):
        """
        1. service belongs to business
        2. check business working schedule
        3. check overlapping bookings
        """
        service = data["service"]
        business = data["business"]
        start_time = data["start_time"]
        duration = service.duration_minutes
        end_time = start_time + timedelta(minutes=duration)

        # 1) Service must belong to the same business
        if service.business_id != business.id:
            raise serializers.ValidationError("This service does not belong to this business.")

        # 2) Check working schedule (basic version)
        from schedules.models import WorkingHours  # ще го направим след малко

        weekday = start_time.weekday()  # 0=Monday
        working = WorkingHours.objects.filter(business=business, weekday=weekday).first()

        if not working or start_time.time() < working.start_time or end_time.time() > working.end_time:
            raise serializers.ValidationError("Booking is outside working hours.")

        # 3) Overlapping logic
        overlaps = Booking.objects.filter(
            business=business,
            service=service,
            start_time__lt=end_time,
            end_time__gt=start_time,
            status__in=["pending", "confirmed"]
        )

        if overlaps.exists():
            raise serializers.ValidationError("This time slot is already booked.")

        return data
