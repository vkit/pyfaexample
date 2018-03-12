from django.contrib import admin

from models import JobSpec
from process.models import Process


class ProcessInline(admin.TabularInline):
    model = Process


class JobSpecAdmin(admin.ModelAdmin):

    list_display = (
        'number', 'customer', 'name', 'total_estimated_time',
        'delivery_qty', 'created_at', 'updated_at')
    search_fields = ['number']
    date_hierarchy = 'created_at'
    list_filter = ['created_at']

    inlines = [
        ProcessInline,
    ]


admin.site.register(JobSpec, JobSpecAdmin)
