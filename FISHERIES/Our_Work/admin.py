from django.contrib import admin
from .models import OurWork


@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = (
        'author_name',
        'position',
        'is_active',
        'created_at'
    )
    list_filter = (
        'is_active',
        'created_at'
    )
    search_fields = (
        'author_name',
        'position',
        'message'
    )
    list_editable = ('is_active',)
