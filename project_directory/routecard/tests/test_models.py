from django.test import TestCase
from django.utils import timezone

from routecard.factories import RouteCardFactory, RouteCardReportFactory, PlanFactory
from routecard.models import RouteCard, RouteCardReport


class RouteCardTest(TestCase):

    def setUp(self):
        self.routecard = RouteCardFactory()

    def test_routecard_creation(self):
        self.assertTrue(isinstance(self.routecard, RouteCard))

    def test_process_sequence(self):
        print self.routecard.process_sequence()

    

class RouteCardReportTest(TestCase):

    def setUp(self):
        self.routecardreport = RouteCardReportFactory()
        self.routecard = RouteCardFactory()
        self.plan = PlanFactory.create(routecard=self.routecard)
        self.routecardreport1 = RouteCardReportFactory.create(plan=self.plan)
        self.routecardreport2 = RouteCardReportFactory.create(plan=self.plan)

    def test_routecardreport_creation(self):
        self.assertTrue(isinstance(self.routecardreport, RouteCardReport))

    def test_total_accepted_quantity(self):
        self.assertEqual(self.plan.total_accepted_quantity(), 100)

    def test_plan_completed(self):
        self.assertTrue(self.plan.plan_completed())


class RouteCardOpenPlanTest(TestCase):


    def setUp(self):
        self.routecard = RouteCardFactory()
        self.plan1 = PlanFactory(
            routecard=self.routecard,
            planned_on=timezone.now()+timezone.timedelta(days=1))
        self.plan2 = PlanFactory(
            routecard=self.routecard,
            planned_on=timezone.now()+timezone.timedelta(days=2))
        self.plan3 = PlanFactory(
            routecard=self.routecard,
            planned_on=timezone.now()+timezone.timedelta(days=3))
        self.plan4 = PlanFactory(
            routecard=self.routecard,
            planned_on=timezone.now()+timezone.timedelta(days=4))
        self.report = RouteCardReportFactory(
            plan=self.plan1,
            production_qty=100)



    def test_routecard_open_plan(self):
        print self.routecard.open_plan()


    


class PlanSaveTest(TestCase):

    def setUp(self):
        self.routecard = RouteCardFactory()
        self.plan = PlanFactory(
            routecard=self.routecard,
            planned_on=timezone.now()+timezone.timedelta(days=1),
            is_complete=False)


    def test_plan_save_method(self):
        report = RouteCardReportFactory(
                plan=self.plan,
                production_qty=100)
        self.assertTrue(self.plan.is_complete)

    def test_is_planned(self):
        print self.plan.is_planned()
    

