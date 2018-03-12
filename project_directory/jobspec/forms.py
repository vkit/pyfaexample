from django import forms
from .models import JobSpec
from process.models import Process


class JobSpecForm(forms.ModelForm):
    class Meta:
        model = JobSpec
        fields = ('number', 'customer', 'name', 'delivery_qty')


class ProcessDisplayForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('process', 'estimated_time','estimated_setting_time', 'remark')


class ProcessCreationForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('jobspec', 'process', 'estimated_time','estimated_setting_time', 'remark')
