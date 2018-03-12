from django.contrib.auth.mixins import PermissionRequiredMixin

from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView
from base.views import GenericModalCreateView, GenericModalUpdateView

from django.views.generic import TemplateView
from .models import Customer
from .forms import CustomerForm


class CustomerListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Customer
    template_name = 'customer/customer_list.html'
    list_display = (
        ('Contact Name', 'contact_name'),
        ('Company Name', 'company_name'),
        ('Credit Days', 'credit_days'),
        ('Ph Number1', 'ph_number1'),
        ('Ph Number2', 'ph_number2'),
        ('City', 'city'),
    )
    title = 'List of Customer'
    detail_url_reverse = 'customer:detail'
    permission_required = 'customer.add_customer'

    def get_context_data(self, **kwargs):
        context = super(
            CustomerListView, self).get_context_data(**kwargs)
        context['form'] = CustomerForm()
        return context


class CustomerModalCreateView(
    PermissionRequiredMixin, GenericModalCreateView
):

    form_class = CustomerForm
    success_url = '/customer/list/'
    object_name = 'Customer'
    permission_required = 'customer.add_customer'


class CustomerDetailView(
    PermissionRequiredMixin, GeneralContextMixin,
    TemplateView
):
    model = Customer
    template_name = 'customer/customer_detail.html'
    permission_required = 'customer.add_customer'

    def get_context_data(self, **kwargs):
        context = super(
            CustomerDetailView, self).get_context_data(**kwargs)
        context['customer'] = Customer.objects.get(pk=self.kwargs.get('pk'))
        context['form'] = CustomerForm(instance=context['customer'])
        return context


class CustomerEditView(
    PermissionRequiredMixin, GenericModalUpdateView
):

    permission_required = 'customer.add_customer'
    form_class = CustomerForm
    object_name = 'customer'
    model = Customer
    app_url = '/customer/'
    page_url = '/detail/'
