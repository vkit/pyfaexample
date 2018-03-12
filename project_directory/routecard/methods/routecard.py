from django.utils import timezone

from django.db.models import Max

import logging
logger = logging.getLogger(__name__)


def __str__(self):
    return "{0}-{1}".format(
        self.jobspec.number, self.number
    )


def process_sequence(self):
    for plan in self.plan_set.all():
        print plan


def total_estimated_time(self):
    time = 0
    for process in self.jobspec.process_set.all():
        time += (process.estimated_cycle_hours() * self.quantity)
        time += process.estimated_setting_hours()
    return time


def save(self, *args, **kwargs):

    # for automatic generating numbers

    if self.jobspec.routecard_set.count() == 0:
        self.number = 1
    else:
        self.number = self.jobspec.routecard_set.latest('created_at').number + 1
    return super(self.__class__, self).save(*args, **kwargs)


def planned_finish_time(self):
    return self.plan_set.aggregate(Max('planned_on'))['planned_on__max']


def expected_finish_time(self):
    """
    Calulates the acutal finish time based on time recorded in
    routecard reports"""
    pass


def open_plan(self):
    """
    Returns plan object that is allowed for reporting
    """

    if not all([plan.is_planned() for plan in self.plan_set.iterator()]):
        logger.debug('Here')
        return self.plan_set.earliest('planned_on')
    if self.is_planned():
        try:
            return self.plan_set.filter(
                is_complete=False).earliest('planned_on')
        except:
            pass


def is_planned(self):
    """
    Return True if all the plans have planned_on datetime
    """
    return not None in [plan.planned_on for plan in self.plan_set.all()]

