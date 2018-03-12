import factory

# from django.contrib.auth.models import User

from factory.django import DjangoModelFactory

from .models import Customer


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    company_name = factory.Sequence(lambda n: 'ComapnyName%d' % n)
    contact_name = "sdfsdf"
    credit_days = 12
