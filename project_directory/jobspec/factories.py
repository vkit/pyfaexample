from factory.django import DjangoModelFactory

import factory

from models import JobSpec

from customer.factories import CustomerFactory
from process.factories import ProcessFactory


class JobSpecFactory(DjangoModelFactory):
    class Meta:
        model = JobSpec

    number = factory.Sequence(lambda n: 'JS%d' % n)
    customer = factory.SubFactory(CustomerFactory)
    name = "SomeName"
    delivery_qty = 100
    process = factory.RelatedFactory(ProcessFactory, 'jobspec')
    process1 = factory.RelatedFactory(ProcessFactory, 'jobspec')
