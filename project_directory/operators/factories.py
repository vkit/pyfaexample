from factory.django import DjangoModelFactory


from models import Operator


class OperatorFactory(DjangoModelFactory):
    class Meta:
        model = Operator

    name = 'raghu'
