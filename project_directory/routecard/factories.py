from factory.django import DjangoModelFactory

import factory
from django.utils import timezone

from .models import RouteCard, Plan, RouteCardReport

from jobspec.factories import JobSpecFactory
from operators.factories import OperatorFactory
from process.factories import ProcessFactory
from machine.factories import MachineFactory


class RouteCardFactory(DjangoModelFactory):
    class Meta:
        model = RouteCard

    number = factory.Sequence(lambda n: 'RC%d' % n)
    quantity = 100
    jobspec = factory.SubFactory(JobSpecFactory)


class PlanFactory(DjangoModelFactory):

    class Meta:
        model = Plan

    process = factory.SubFactory(ProcessFactory)
    routecard = factory.SubFactory(RouteCardFactory)
    machine = factory.SubFactory(MachineFactory)
    planned_on = timezone.now()
    is_complete = False


class RouteCardReportFactory(DjangoModelFactory):
    class Meta:
        model = RouteCardReport
    shift = 2
    production_qty = 50
    rejection_qty = 50
    operator = factory.SubFactory(OperatorFactory)
    start_time = timezone.now()
    end_time = timezone.now() + timezone.timedelta(hours=1)
    plan = factory.SubFactory(PlanFactory)
