from django.contrib.auth.mixins import PermissionRequiredMixin

from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView
from base.views import GenericModalCreateView

from .models import Operator
from .forms import OperatorForm


class OperatorsListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Operator
    template_name = 'operators/operators_list.html'
    list_display = (
        ('Name', 'name'),
    )
    title = 'List of Operators'
    sub_title = ''
    date_range = False
    detail_url_reverse = ''
    check_box = True
    action_dict = None
    edit = False
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            OperatorsListView, self).get_context_data(**kwargs)
        context['form'] = OperatorForm()
        return context


class OperatorModalCreateView(
    PermissionRequiredMixin, GenericModalCreateView
):

    form_class = OperatorForm
    success_url = '/operators/list/'
    object_name = 'JobSpec'
    error_url = None
    permission_required = 'operator.add_operator'

