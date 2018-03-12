from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect

from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView
from base.views import GenericModalCreateView, GenericModalUpdateView
from django.views.generic import TemplateView
from .models import Machine
from .forms import MachineForm, MachineEditDetailForm, TimeQuantaForm

from routecard.models import Plan
from routecard.views import PlanListView


class MachineListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Machine
    template_name = 'machine/machine_list.html'
    list_display = (
        ('Name', 'name'),
        ('Total Process Count', 'total_process_count')
    )
    title = 'List of Machines'
    permission_required = 'jobspec.add_jobspec'
    detail_url_reverse = 'machine:machine_plans'

    def get_context_data(self, **kwargs):
        context = super(
            MachineListView, self).get_context_data(**kwargs)
        context['form'] = MachineForm()
        return context


class MachineModalCreateView(
    PermissionRequiredMixin, GenericModalCreateView
):

    form_class = MachineForm
    success_url = '/machine/list/'
    object_name = 'Machine'
    error_url = None
    permission_required = 'machine.add_machine'


def getMachine(request):
    print request.GET.get('machine')
    machine = Machine.objects.get(pk=request.GET.get('machine'))
    schedule_list = machine.schedule_list()
    print schedule_list
    return HttpResponse(
        str(schedule_list),
    )


# class MachineDetailView(
#     PermissionRequiredMixin, GeneralContextMixin,
#     TemplateView
# ):
#     model = Machine
#     template_name = 'machine/machine_detail.html'
#     permission_required = 'customer.add_customer'

#     def get_context_data(self, **kwargs):
#         context = super(
#             MachineDetailView, self).get_context_data(**kwargs)
#         context['machine'] = Machine.objects.get(pk=self.kwargs.get('pk'))
#         context['form'] = MachineEditDetailForm(instance=context['machine'])
#         return context

class MachineDetailView(PlanListView):

    template_name = 'machine/machine_plans.html'

    def make_query(self, **kwargs):
        plans = Plan.objects.filter(machine__pk=self.kwargs.get('pk'))
        return plans

    def get_context_data(self, **kwargs):
        context = super(
            MachineDetailView, self).get_context_data(**kwargs)
        context['machine'] = Machine.objects.get(pk=self.kwargs.get('pk'))
        context['form'] = MachineEditDetailForm(instance=context['machine'])
        return context


class MachineDetailEditView(
    PermissionRequiredMixin, GenericModalUpdateView
):

    permission_required = 'customer.add_customer'
    form_class = MachineEditDetailForm
    object_name = 'Machine'
    model = Machine
    app_url = '/machine/'
    page_url = '/machine_plans/'

    def get_success_url(self):
        return '/machine/machine_plans/{0}'.format(self.kwargs.get('pk'))

