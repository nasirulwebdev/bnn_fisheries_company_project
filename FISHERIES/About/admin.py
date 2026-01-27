from django.contrib import admin
from .models import AboutPage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'created_at'
    )
    list_filter = (
        'is_active',
        'created_at'
    )
    search_fields = (
        'title',
        'short_description'
    )
    list_editable = (
        'is_active',
    )
