from django.contrib import admin

from models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'credit_days')
    search_fields = ['company_name']

admin.site.register(Customer, CustomerAdmin)
