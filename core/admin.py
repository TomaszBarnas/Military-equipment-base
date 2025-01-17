from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'resource_type', 'quantity', 'status', 'location', 'created_at', 'updated_at')  # Columns to display
    search_fields = ('name', 'resource_type', 'status')  # Enable search
    list_filter = ('resource_type', 'status')  # Add filters
