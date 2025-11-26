from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    business = serializers.ReadOnlyField(source='business.id')

    class Meta:
        model = Service
        fields = [
            "id",
            "business",
            "name",
            "description",
            "price",
            "duration_minutes",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]