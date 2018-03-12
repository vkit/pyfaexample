from factory.django import DjangoModelFactory

import factory

from models import Machine


class MachineFactory(DjangoModelFactory):
    class Meta:
        model = Machine

    name = factory.Sequence(lambda n: 'Machine%d' % n)