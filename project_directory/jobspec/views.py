from django.shortcuts import HttpResponseRedirect

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from django.forms import inlineformset_factory

from base.mixin import GeneralContextMixin
from base.views import GenericDataGridView, GenericSelfRedirection, GenericModalUpdateView

from process.models import Process
from process.forms import ProcessForm, ProcessNameForm
from routecard.forms import RouteCardForm, RouteCardDisplayForm

from .models import JobSpec
from routecard.models import RouteCard, Plan
from .forms import JobSpecForm, ProcessCreationForm, ProcessDisplayForm


class JobSpecListView(
    GeneralContextMixin, PermissionRequiredMixin,
    GenericDataGridView
):
    model = JobSpec
    template_name = 'jobspec/jobspec_list.html'
    list_display = (
        ('Number', 'number'),
        ('Customer', 'customer'),
        ('Name', 'name'),
        ('Total estimated time (Hrs.)', 'total_estimated_time'),
        ('Total Processes', 'total_processes'),
        ('Delivery Qty', 'delivery_qty'),
        ('Created', 'created_at'),
    )
    title = 'List of JobSpec'
    sub_title = ''
    date_range = False
    detail_url_reverse = 'jobspec:detail'
    check_box = True
    action_dict = None
    action_dict = {'Delete': 'delete'}
    edit = False
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            JobSpecListView, self).get_context_data(**kwargs)
        context['form'] = JobSpecForm()
        return context

    def delete(self):
        jobspecs = JobSpec.objects.filter(pk__in=self.for_action_keys)
        for jobspec in jobspecs:
            if not jobspec.routecard_set.exists():
                jobspec.delete()
            messages.warning(
                self.request, 'Selected JobSpec are succesfully deleted')
        return HttpResponseRedirect(reverse('jobspec:list'))


class JobSpecCreateView(
    GeneralContextMixin, PermissionRequiredMixin, TemplateView
):

    parent_model = JobSpec
    child_model = Process
    child_form_class = ProcessForm
    extra = 1
    fields = ('process', 'estimated_time', 'estimated_setting_time', 'remark')
    template_name = 'jobspec/jobspec_create.html'
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            JobSpecCreateView, self).get_context_data(**kwargs)
        context['form'] = JobSpecForm()
        process_set_form = inlineformset_factory(
            self.parent_model, self.child_model,
            extra=self.extra,
            fields=self.fields,
            can_delete=False
        )
        context['process_set_form'] = process_set_form()
        context['extra'] = self.extra
        context['form1'] = ProcessNameForm()
        context['child_model'] = self.child_model._meta.verbose_name
        return context

    def post(self, request, *args, **kwargs):
        print request.POST
        from django.contrib import messages
        process_set_form = inlineformset_factory(
            self.parent_model, self.child_model,
            extra=request.POST['process_set-TOTAL_FORMS'],
            fields=self.fields,
            can_delete=False,
        )
        form = JobSpecForm(request.POST)
        if form.is_valid():
            print "valid form"
            jobspec = form.save()
            formset = process_set_form(request.POST, instance=jobspec)
            if formset.is_valid():
                print "valid formset"
                formset.save()
                messages.success(request, "New Jobspec %s created" % jobspec)
                return HttpResponseRedirect('/jobspec/list')
            else:
                print "formset not vaild"
                messages.warning(request, formset.errors)
                return HttpResponseRedirect('/jobspec/create')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/jobspec/create')


class JobSpecDetailEditView(
    PermissionRequiredMixin, GenericModalUpdateView
):

    permission_required = 'jobspec.add_jobspec'
    form_class = JobSpecForm
    object_name = 'jobspec'
    model = JobSpec

    def get_success_url(self):
        return '/jobspec/detail/{0}'.format(self.kwargs.get('pk'))


class JobSpecDetailView(
    PermissionRequiredMixin, GeneralContextMixin,
    GenericDataGridView
):
    model = Process
    template_name = 'jobspec/jobspec_detail.html'
    list_display = (
        ('Process', 'process'),
        ('Estimated Time', 'estimated_time'),
        ('Estimated Setting Time', 'estimated_setting_time'),
        ('Remark', 'remark'),
    )
    title = 'List of Processes'
    action_dict = {'Delete': 'delete'}
    edit = True
    permission_required = 'jobspec.add_jobspec'

    def get_context_data(self, **kwargs):
        context = super(
            JobSpecDetailView, self).get_context_data(**kwargs)
        context['jobspec'] = JobSpec.objects.get(pk=self.kwargs.get('pk'))
        context['form1'] = ProcessDisplayForm()
        context['form'] = JobSpecForm(instance=context['jobspec'])
        context['form2'] = RouteCardDisplayForm()
        return context

    def delete(self):
        process = Process.objects.filter(pk__in=self.for_action_keys)
        print "+++++"
        print process
        print "_____"
        var = process.delete()
        print var
        messages.warning(
            self.request, 'Selected Process are succesfully deleted')
        return HttpResponseRedirect('/jobspec/detail/{0}'.format(self.kwargs.get('pk')))    

    def make_query(self, **kwargs):
        processes = Process.objects.filter(jobspec__pk=self.kwargs.get('pk'))
        return processes


class ProcessModalCreateView(
    PermissionRequiredMixin, GenericSelfRedirection
):

    form_class = ProcessCreationForm
    url_pattern_list = ['jobspec', 'detail']
    object_name = 'Process'
    error_url = None
    permission_required = 'jobspec.add_jobspec'

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['jobspec'] = kwargs.get('pk')
        form = ProcessCreationForm(data)
        print form
        return self.form_check(form, *args, **kwargs)

    def get_success_url(self):
        return '/jobspec/detail/{0}'.format(self.kwargs.get('pk'))


class RouteCardGenerateModalCreateView(
    PermissionRequiredMixin,
    GenericSelfRedirection
):
    form_class = RouteCardForm
    object_name = 'RouteCard'
    template_name = 'jobspec/jobspec_detail.html'
    permission_required = 'jobspec.add_jobspec'
    url_pattern_list = ['routecard', 'detail']
    error_url = '/jobspec/list/'

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['jobspec'] = kwargs.get('pk')
        form = RouteCardForm(data)
        return self.form_check(form, *args, **kwargs)

    def get_success_url(self):
        jobspec = JobSpec.objects.get(pk=self.kwargs.get('pk'))
        processes = jobspec.process_set.all()
        routecard = RouteCard.objects.get(pk=self.pk_id)
        for process in processes:
            Plan.objects.create(
                process=process,
                routecard=routecard)
        return super(RouteCardGenerateModalCreateView, self).get_success_url()

