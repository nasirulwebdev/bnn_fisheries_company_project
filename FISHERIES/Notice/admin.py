from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'priority',
        'is_active',
        'created_at'
    )

    list_filter = (
        'priority',
        'is_active',
        'created_at'
    )

    search_fields = ('title', 'description')

    list_editable = ('is_active',)

    readonly_fields = ('created_at',)

    fieldsets = (
        ('Notice Information', {
            'fields': (
                'title',
                'description',
                'file'
            )
        }),

        ('Status Settings', {
            'fields': (
                'priority',
                'is_active'
            )
        }),

        ('Date Information', {
            'fields': ('created_at',)
        }),
    )