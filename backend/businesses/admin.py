from django.contrib import admin
from .models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "phone", "created_at")
    search_fields = ("name", "owner__email")
    list_filter = ("created_at",)
    prepopulated_fields = {"slug": ("name",)}