from django.contrib import admin
from .models import Company, Device, Employee, DeviceAssignment

# Configuration for site-wide admin panel attributes.
admin.site.site_header = "Asset Tracker API"
admin.site.site_title = "Corporate Asset Tracker Django REST API"
admin.site.index_title = "Welcome Admin"

# Common AdminMixin for shared configurations.
class CommonAdminMixin(admin.ModelAdmin):
    pass  # Any shared functionality would go here.


@admin.register(Company)
class CompanyAdmin(CommonAdminMixin):
    """Admin interface for the Company model."""
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(CommonAdminMixin):
    """Admin interface for the Device model."""
    list_display = ('name', 'serial_number', 'condition', 'company', 'checked_out')
    search_fields = ('name', 'serial_number')


@admin.register(Employee)
class EmployeeAdmin(CommonAdminMixin):
    """Admin interface for the Employee model."""
    search_fields = ('company', 'devices')


@admin.register(DeviceAssignment)
class DeviceAssignmentAdmin(CommonAdminMixin):
    """Admin interface for the DeviceAssignment model."""
    list_display = ('device', 'employee', 'assigned_date', 'return_date', 'updated_at')
    search_fields = ('device', 'employee__name')
