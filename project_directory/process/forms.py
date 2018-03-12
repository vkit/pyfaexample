from django import forms
from .models import Process, ProcessName


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('process', 'estimated_time', 'jobspec', 'remark')


class ProcessNameForm(forms.ModelForm):
    class Meta:
        model = ProcessName
        fields = ('name', )
