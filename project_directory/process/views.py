from django.contrib.auth.mixins import PermissionRequiredMixin

from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView
from base.views import GenericModalCreateView

from .models import Process
from .forms import ProcessForm, ProcessNameForm


class ProcessListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Process
    template_name = 'process/process_list.html'
    list_display = (
        ('Process', 'process'),
        ('Estimated_time', 'estimated_time'),
        ('JobSpec', 'jobspec'),
    )
    title = 'List of Process'
    sub_title = ''
    date_range = False
    detail_url_reverse = ''
    check_box = True
    action_dict = None
    edit = False
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            ProcessListView, self).get_context_data(**kwargs)
        context['form'] = ProcessForm()
        context['form1'] = ProcessNameForm()
        return context


class ProcessModalCreateView(
    PermissionRequiredMixin, GenericModalCreateView
):

    form_class = ProcessForm
    success_url = '/process/list/'
    object_name = 'Process'
    error_url = None
    permission_required = 'process.add_process'


class ProcessNameModalCreateView(
    PermissionRequiredMixin, GenericModalCreateView
):

    form_class = ProcessNameForm
    success_url = '/jobspec/create/'
    object_name = 'Process Name'
    error_url = None
    permission_required = 'process.add_process'
