from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publication_date',
        'is_active',
        'created_at'
    )
    list_filter = (
        'is_active',
        'publication_date'
    )
    search_fields = (
        'title',
        'author',
        'description'
    )
    list_editable = ('is_active',)
