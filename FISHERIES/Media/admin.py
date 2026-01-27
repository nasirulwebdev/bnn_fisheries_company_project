from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'media_type',
        'is_active',
        'created_at'
    )
    list_filter = (
        'media_type',
        'is_active'
    )
    search_fields = (
        'title',
        'short_description'
    )
    list_editable = (
        'is_active',
    )
