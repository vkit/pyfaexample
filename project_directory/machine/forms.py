from django import forms
from .models import Machine
from routecard.models import TimeQuanta


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('name', )


class MachineEditDetailForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('name', )


class TimeQuantaForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )

    def __init__(self, *args, **kwargs):
        self.machine = kwargs.pop('machine', None)
        return super(TimeQuantaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TimeQuanta
        fields = ('start_time', 'plan')

    def clean(self):
        cleaned_data = super(TimeQuantaForm, self).clean()
        cleaned_date = cleaned_data.get('start_time')
        if not self.machine.check_availability(date=cleaned_date):
            msg = "Warning!! Please replan, {0} is not available on selected time {1}".format(
                self.machine, cleaned_data.get('start_time'))
            self.add_error('start_time', msg)

