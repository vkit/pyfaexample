from django.test import TestCase
from jobspec.factories import JobSpecFactory, JobSpec


class JobSpecTest(TestCase):

    def setUp(self):
        self.jobspec = JobSpecFactory()

    def test_jobspec_creation(self):
        self.assertTrue(isinstance(self.jobspec, JobSpec))

    def test_total_estimated_time(self):
        self.assertEquals(
            self.jobspec.total_estimated_time(),
            22.0
        )

    def test_total_processes(self):
        self.assertEquals(self.jobspec.total_processes(), 2)


