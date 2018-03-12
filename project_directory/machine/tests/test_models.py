from django.test import TestCase
from django.utils import timezone
from machine.factories import MachineFactory, Machine

from routecard.factories import RouteCardFactory, PlanFactory


class MachineTest(TestCase):

    def setUp(self):
        self.machine = MachineFactory()
        print self.machine

    def test_machine_creation(self):
        self.assertTrue(isinstance(self.machine, Machine))


# class MachineLoadTest(TestCase):

#     def setUP(self):
#         self.rc = RouteCardFactory()

#     def test_load(self):
#         machines = Machine.objects.all()
#         for machine in machines:
#             print machine.load()


class MachineScheduleTest(TestCase):

    def setUp(self):
        self.machine1 = MachineFactory()
        self.machine2 = MachineFactory()
        self.rc = RouteCardFactory()
        self.processes = self.rc.jobspec.process_set.all()
        print self.processes
        self.plan1 = PlanFactory(
            routecard=self.rc,
            process=self.processes[0],
            machine=self.machine1,
            time=timezone.now() + timezone.timedelta(days=1)
        )
        self.plan2 = PlanFactory(
            routecard=self.rc,
            process=self.processes[1],
            machine=self.machine1,
            time=timezone.now() + timezone.timedelta(days=2)
        )

    def test_schedule_list(self):
        print "XXXX"
        print self.machine1.schedule_list()
        # print self.machine2.schedule_list()

