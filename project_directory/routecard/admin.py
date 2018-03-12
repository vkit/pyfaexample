from django.contrib import admin

from models import RouteCard, RouteCardReport, Plan, TimeQuanta


class RouteCardReportInline(admin.TabularInline):
    model = RouteCardReport


class PlanInline(admin.TabularInline):
    model = Plan


class TimeQuantaInline(admin.TabularInline):
    model = TimeQuanta


class PlanAdmin(admin.ModelAdmin):

    list_display = (
        'process', 'routecard', 'machine',
        'planned_on', 'end_time',
        'created_at', 'updated_at')
    # search_fields = ['number']
    date_hierarchy = 'created_at'
    list_filter = ['created_at']
    inlines = [
        TimeQuantaInline,
    ]


class RouteCardAdmin(admin.ModelAdmin):

    list_display = (
        '__str__', 'quantity', 'total_estimated_time',
        'created_at', 'updated_at')
    search_fields = ['number']
    date_hierarchy = 'created_at'
    list_filter = ['created_at']

    inlines = [
        PlanInline,
    ]


admin.site.register(RouteCard, RouteCardAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(RouteCardReport)
