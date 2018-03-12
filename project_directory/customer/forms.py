from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'contact_name', 'company_name', 'pan_no', 'tin_no',
            'service_tax_no', 'credit_days', 'ph_number1',
            'ph_number2', 'addressline1', 'addressline2',
            'email', 'zipcode', 'city', 'state', 'country'
        )
