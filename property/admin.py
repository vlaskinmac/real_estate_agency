from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
