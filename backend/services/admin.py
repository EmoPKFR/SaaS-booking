from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'price', 'duration_minutes', 'created_at')
    search_fields = ('name', 'business__name')
    list_filter = ('business', 'created_at')
    readonly_fields = ('created_at', 'updated_at')