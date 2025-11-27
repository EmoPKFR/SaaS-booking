from rest_framework import serializers
from .models import Business


class BusinessSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Business
        fields = [
            'id', 'owner', 'name', 'slug', 'address', 
            'phone', 'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']