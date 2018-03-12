from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import View

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse


from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView, GenericSelfRedirection, GenericModalUpdateView, GenericModalCreateView
from django.views.generic import TemplateView
from .models import RouteCard, Plan, RouteCardReport
from .forms import (
    RouteCardForm, PlanForm,
    RouteCardReportForm, PlanEditForm,
    RouteCardReportDisplayForm, RouteCardEditForm, TimeQuantaForm
)
from machine.models import Machine


class RouteCardListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = RouteCard
    template_name = 'routecard/routecard_list.html'
    list_display = (
        ('Number', '__str__'),
        ('Name', 'jobspec.name'),
        ('Quantity', 'quantity'),
        ('P.O No', 'po_no'),
        ('Delivery Date', 'delivery_date', ),
        ('Next open plan', 'open_plan'),
        ('Planned Finish time', 'planned_finish_time'),
    )
    title = 'List of RouteCard'
    edit = True
    detail_url_reverse = 'routecard:detail'
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            RouteCardListView, self).get_context_data(**kwargs)
        context['form'] = RouteCardForm()
        return context

# Print all the plans


class PrintPLanView(View):
    def post(self, request, *args, **kwargs):
        routecard = RouteCard.objects.get(pk=self.kwargs.get('pk'))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={0}-{1}.csv'.format(routecard.jobspec.number,routecard.number)
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))
        # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
           smart_str(u"Process"),
           smart_str(u"Machine"),
           smart_str(u"Planned Start Time"),
           smart_str(u"Planned End Time"),
           smart_str(u"Completed"),
           smart_str(u"Total Accepted"),
           smart_str(u"Delay"),
        ])
        for plan in routecard.plan_set.all():
            writer.writerow([
               smart_str(plan.process),
               smart_str(plan.machine),
               smart_str(plan.planned_on),
               smart_str(plan.end_time()),
               smart_str(plan.is_complete),
               smart_str(plan.total_accepted_quantity()),
               smart_str(plan.delay()),
           ])
        return response

 
class RouteCardModalCreateView(
    PermissionRequiredMixin,
    GenericSelfRedirection
):
    form_class = RouteCardForm
    object_name = 'RouteCard'
    permission_required = 'routecard.add_routecard'
    url_pattern_list = ['routecard', 'detail']
    error_url = '/routecard/list/'

    def get_success_url(self):
        routecard = get_object_or_404(RouteCard, pk=self.pk_id)
        jobspec = routecard.jobspec
        processes = jobspec.process_set.all()
        for process in processes:
            Plan.objects.create(
                process=process,
                routecard=routecard)
        if self.url_pattern_list is None:
            raise ImproperlyConfigured(
                "GenericModalCreateView requires either a definition of "
                "'success_url'")
        url_pattern = '/'.join(self.url_pattern_list)
        return "/{0}/{1}".format(
            url_pattern, self.pk_id)


class RouteCardDetailView(
    PermissionRequiredMixin, GeneralContextMixin,
    GenericDataGridView
):
    model = Plan
    template_name = 'routecard/routecard_detail.html'
    list_display = (
        ('Process', 'process'),
        ('Machine', 'machine'),
        ('Planned Start Time', 'planned_on'),
        ('Planned End Time', 'end_time'),
        ('Completed', 'is_complete'),
        ('Total Accepted', 'total_accepted_quantity'),
        ('Delay', 'delay'),
    )
    title = 'List of Plan'
    permission_required = 'routecard.add_routecard'
    action_dict = {'Delete': 'delete'}
    edit = True
    action_column_name = "RePlan"
    action_column_dict = {}

    def get(self, request, *args, **kwargs):
        routecard = RouteCard.objects.get(pk=self.kwargs.get('pk'))
        if routecard.is_planned():
            self.action_column_dict['Add Report'] = '/routecard/report_detail/'
        return super(RouteCardDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            RouteCardDetailView, self).get_context_data(**kwargs)
        routecard = get_object_or_404(RouteCard, pk=self.kwargs.get('pk'))
        context['routecard'] = routecard
        context['plans'] = Plan.objects.filter(routecard=routecard)
        context['form'] = PlanEditForm()
        context['form1'] = RouteCardEditForm(instance=context['routecard'])
        context['plan_form'] = PlanForm(route_card=routecard)
        return context

    def delete(self):
        print self.for_action_keys
        plan = Plan.objects.filter(pk__in=self.for_action_keys)
        plan.delete()
        messages.warning(
            self.request, 'Selected JobSpec are succesfully deleted')
        return HttpResponseRedirect(
            '/routecard/detail/{0}'.format(self.kwargs.get('pk')))

    def make_query(self, **kwargs):
        routecard = RouteCard.objects.get(pk=self.kwargs.get('pk'))
        plans = Plan.objects.filter(routecard=routecard).order_by('created_at')
        return plans


class RouteCardDetailEditView(
    PermissionRequiredMixin, GenericModalUpdateView
):

    permission_required = 'jobspec.add_jobspec'
    form_class = RouteCardEditForm
    object_name = 'routecard'
    model = RouteCard

    def get_success_url(self):
        return '/routecard/detail/{0}'.format(self.kwargs.get('pk'))


class PlanModalCreateView(
    PermissionRequiredMixin,
    GenericModalCreateView
):

    form_class = PlanForm
    object_name = 'Plan'
    permission_required = 'routecard.add_routecard'

    def get_success_url(self):
        return '/routecard/detail/{0}'.format(self.kwargs.get('pk'))


class PlanListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Plan
    template_name = 'routecard/plan_list.html'
    list_display = (
        ('Process', 'process'),
        ('Routecard', 'routecard'),
        ('Machine', 'machine'),
        ('Planned Start Time', 'planned_on'),
        ('Planned End Time', 'end_time'),
        ('Plan Completed', 'plan_completed'),
    )
    title = 'List of Plan'
    detail_url_reverse = 'routecard:report_detail'
    edit = True
    permission_required = 'jobspec.add_jobspec'
    action_column_name = "Add Report"


class OperatorMachineListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = Machine
    template_name = 'routecard/operator_plan_list.html'
    list_display = (
        ('Machine', 'name'),
        ('Planned Processes ', 'total_process_count')
    )
    title = 'List of Machines'
    detail_url_reverse = 'routecard:plan_detail'
    permission_required = 'routecard.add_plan'


class OperatorPlanDetailView(
    PermissionRequiredMixin, GeneralContextMixin,
    GenericDataGridView
):
    model = Plan
    template_name = 'routecard/plan_detail.html'
    list_display = (
        ('process', 'process'),
        ('Routecard', 'routecard'),
        ('Estimated Start Time', 'start_time'),
        ('Estimated End Time', 'end_time'),
        ('Plan Completed', 'plan_completed')
    )
    title = 'List of Plans'
    detail_url_reverse = 'routecard:report_detail'
    permission_required = 'routecard.add_routecardreport'
    
    def make_query(self, **kwargs):
        return self.model.objects.filter(
            machine__pk=self.kwargs.get('pk')).order_by('-created_at')

# routecard report


class OperatorRouteCardReportDetailView(
    PermissionRequiredMixin, GeneralContextMixin,
    GenericDataGridView
):
    model = RouteCardReport
    action_dict = {'Delete': 'delete'}
    edit = True
    template_name = 'routecard/operator_detail.html'
    list_display = (
        ('Shift', 'shift'),
        ('Production Quantity', 'production_qty'),
        ('Rejection Quantity', 'rejection_qty'),
        ('Operator', 'operator'),
        ('Start Time', 'start_time'),
        ('End Time', 'end_time'),

    )
    permission_required = 'routecard.add_routecardreport'

    def get_context_data(self, **kwargs):
        context = super(
            OperatorRouteCardReportDetailView, self).get_context_data(**kwargs)
        plan = Plan.objects.get(pk=self.kwargs.get('pk'))
        context['plan'] = plan
        context['routecardreport'] = RouteCardReport.objects.filter(plan=plan)
        context['form'] = RouteCardReportDisplayForm()
        return context

    def delete(self):
        print self.for_action_keys
        routecardreport = RouteCardReport.objects.filter(
            pk__in=self.for_action_keys)
        var = routecardreport.delete()
        print var
        messages.warning(
            self.request, 'Selected Report is succesfully deleted')
        return HttpResponseRedirect(
            '/routecard/report_detail/{0}'.format(self.kwargs.get('pk')))

    def make_query(self, **kwargs):
        plan = Plan.objects.get(pk=self.kwargs.get('pk'))
        routecardreport = RouteCardReport.objects.filter(plan=plan)
        return routecardreport


class OperatorRouteCardReportModalCreateView(
    PermissionRequiredMixin,
    GenericSelfRedirection
):

    form_class = RouteCardReportForm
    object_name = 'Routecardreport'
    permission_required = 'routecard.add_routecard'
    url_pattern_list = ['routecard', 'report_detail']

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['plan'] = kwargs.get('pk')
        form = RouteCardReportForm(data)
        return self.form_check(form, *args, **kwargs)

    def get_success_url(self):
        return '/routecard/report_detail/{0}'.format(self.kwargs.get('pk'))


class RePlanView(PermissionRequiredMixin, TemplateView):

    permission_required = 'routecard.add_plan'
    template_name = 'routecard/replan.html'

    def get_context_data(self, **kwargs):
        context = super(
            RePlanView, self).get_context_data(**kwargs)
        machine = Machine.objects.get(pk=self.request.GET.get('machine'))
        context['machine'] = machine
        context['plan'] = self.request.GET.get('plan')
        context['routecard'] = self.request.GET.get('routecard')
        return context

    def post(self, request, *args, **kwargs):
        routecard = request.POST.get('routecard')
        plan = Plan.objects.get(pk=request.POST.get('plan'))
        machine = Machine.objects.get(pk=request.POST.get('machine'))
        form = TimeQuantaForm(request.POST, machine=machine)
        if form.is_valid():
            print "Valid"
            form.save()
            plan.machine = machine
            plan.planned_on = form.cleaned_data.get('start_time')
            plan.save()
            messages.success(
                request, "Plan {0} updated successfully".format(plan))
            return HttpResponseRedirect(
                '/routecard/detail/{0}'.format(routecard)
            )
        else:
            messages.warning(
                request, form.errors)
            return HttpResponseRedirect(
                '/routecard/detail/{0}'.format(routecard)
            )