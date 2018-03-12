from django.test import TestCase
from customer.factories import CustomerFactory
from .models import Customer


class CustomerTest(TestCase):

    def setUp(self):
        self.customer = CustomerFactory()
        print self.customer

    def test_customer_creation(self):
        self.assertEqual(Customer.objects.count(), 1)
        self.assertTrue(isinstance(self.customer, Customer))
