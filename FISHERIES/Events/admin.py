from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'event_type',
        'event_date',
        'location',
        'is_active'
    )
    list_filter = (
        'event_type',
        'event_date',
        'is_active'
    )
    search_fields = (
        'title',
        'location'
    )
    list_editable = (
        'is_active',
    )
