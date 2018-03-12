from django.contrib import admin

from models import Process, ProcessName


class ProcessAdmin(admin.ModelAdmin):

    list_display = (
        'process', 'estimated_time', 'jobspec', 'estimated_cycle_hours',
        'estimated_setting_hours',
        'created_at', 'updated_at')
    search_fields = ['number']
    date_hierarchy = 'created_at'
    list_filter = ['created_at']

admin.site.register(Process, ProcessAdmin)


class ProcessNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ProcessName, ProcessNameAdmin)


