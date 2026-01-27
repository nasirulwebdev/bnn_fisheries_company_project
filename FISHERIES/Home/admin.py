from django.contrib import admin
from .models import Banner, Feature

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'created_at')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at',)
