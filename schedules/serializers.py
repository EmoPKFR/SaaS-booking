from rest_framework import serializers
from .models import WorkingHours


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = "__all__"
        read_only_fields = ["business"]
