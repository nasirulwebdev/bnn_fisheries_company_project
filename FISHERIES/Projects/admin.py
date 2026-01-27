from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'start_date', 'end_date', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'short_description', 'description')
    list_editable = ('is_active',)
    ordering = ('-created_at',)