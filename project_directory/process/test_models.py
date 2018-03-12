from django.test import TestCase
from django.utils import timezone

from process.factories import Process, ProcessFactory


class ProcessTest(TestCase):

    def setUp(self):
        self.process = ProcessFactory(
            estimated_time=timezone.timedelta(minutes=30))
        print self.process

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.process, Process))

    def test_estimated_cycle_hours(self):
        self.assertEqual(self.process.estimated_cycle_hours(), 0.5)

    def test_estimated_setting_hours(self):
        self.assertEqual(self.process.estimated_setting_hours(), 1)
