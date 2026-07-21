from django.contrib import admin
from .models import Device, Company

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'badge_label', 'is_featured', 'verified_by', 'created_at')
    list_filter = ('category', 'is_featured', 'badge_label')
    search_fields = ('name', 'description', 'working_principle', 'maintenance_protocol')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'region', 'email', 'is_leader')
    list_filter = ('region', 'is_leader')
    search_fields = ('name', 'specialization', 'description', 'address')
