from django import forms
from .models import RouteCard, RouteCardReport, Plan, TimeQuanta

from process.models import Process


class RouteCardForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )

    class Meta:
        model = RouteCard
        fields = ('jobspec', 'quantity', 'po_no', 'delivery_date')


class RouteCardDisplayForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )

    class Meta:
        model = RouteCard
        fields = ('quantity', 'po_no', 'delivery_date')


class RouteCardEditForm(forms.ModelForm):
    class Meta:
        model = RouteCard
        fields = ('jobspec', 'quantity')


class RouteCardReportForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )
    end_time = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )

    class Meta:
        model = RouteCardReport
        fields = ('shift', 'production_qty',
                  'rejection_qty', 'operator', 'start_time', 'end_time','plan')


class RouteCardReportDisplayForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )
    end_time = forms.DateTimeField(
        input_formats=('%d/%m/%Y %I:%M %p',)
    )

    class Meta:
        model = RouteCardReport
        fields = ('shift', 'production_qty',
                  'rejection_qty', 'operator', 'start_time', 'end_time')


class PlanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.route_card = kwargs.pop('route_card', None)
        super(PlanForm, self).__init__(*args, **kwargs)
        if self.route_card:
            self.fields['process'].queryset = Process.objects.filter(
                jobspec=self.route_card.jobspec)
            self.initial['routecard'] = self.route_card
            self.fields['routecard'].widget = forms.HiddenInput()

    class Meta:
        model = Plan
        fields = ('process', 'routecard')


class PlanEditForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ('machine',)


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
