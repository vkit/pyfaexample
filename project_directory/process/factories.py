from django.utils import timezone
from factory.django import DjangoModelFactory

import factory

from models import Process, ProcessName


class ProcessNameFactory(DjangoModelFactory):
    class Meta:
        model = ProcessName

    name = factory.Sequence(lambda n: 'Process%d' % n)


class ProcessFactory(DjangoModelFactory):
    class Meta:
        model = Process

    process = factory.SubFactory(ProcessNameFactory)
    estimated_time = timezone.timedelta(hours=0.1)
    estimated_setting_time = timezone.timedelta(hours=1)



