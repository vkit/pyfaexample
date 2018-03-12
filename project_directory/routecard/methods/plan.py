from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError

from base.utils import utc_to_time


def __str__(self):
    return "{0}-{1}".format(self.process, self.machine)


def clean(self):
    if self.process.jobspec.id.hex != self.routecard.jobspec.id.hex:
        raise ValidationError(_(
            'Process selected must belong to same jobspec'))


def total_accepted_quantity(self):
    """
    Calaculates total accepted quantity
    """
    total = 0
    for report in self.reports.all():
        total += report.production_qty
    return total


def plan_completed(self):
    """
    Calaculates if the plan is completed
    """
    if self.total_accepted_quantity() >= self.routecard.quantity:
        return True
    else:
        return False


def formated_time(self):
    """
    Formated time for JS moment method """
    if self.planned_on:
        return 'moment({ y:%d, M:%d, d:%d, h:%d, m:%d})' % (
            utc_to_time(self.planned_on).year,
            utc_to_time(self.planned_on).month - 1,
            utc_to_time(self.planned_on).day,
            utc_to_time(self.planned_on).hour,
            utc_to_time(self.planned_on).minute
        )

def end_time(self):
    """
    Return end time for the plan"""
    if self.planned_on:
        return self.planned_on + self.process.estimated_time * self.routecard.quantity + self.process.estimated_setting_time


def formated_end_time(self):
    """
    Formated time for JS moment method
    """
    if self.end_time() is not None:
        return 'moment({ y:%d, M:%d, d:%d, h:%d, m:%d})' % (
            utc_to_time(self.end_time()).year,
            utc_to_time(self.end_time()).month - 1,
            utc_to_time(self.end_time()).day,
            utc_to_time(self.end_time()).hour,
            utc_to_time(self.end_time()).minute
        )


# def start_time(self):
#     if self.timings.last() is not None:
#         return self.timings.latest('created_at').start_time


def is_active(self):
    if self.reports.exists():
        last_report = self.reports.latest('created_at')
        if last_report.start_time and not last_report.end_time:
            return True
        else:
            return False
    else:
        return False


def actual_end_time(self):
    """
    Returns the end_time recorded in last routecard report
    """
    if self.reports.exists():
        return self.reports.latest('created_at').end_time
    else:
        return self.end_time()


def delay(self):
    if self.reports.exists():
        actual = self.reports.latest('created_at').start_time
    try:
        return actual - self.planned_on
    except:
        return timezone.timedelta(hours=0)


def is_open(self):
    """
    Returns True if a plan is open for reporting by
    operators
    """
    # if self.routecard.is_planned():
    #     for plan in self.routecard.plan_set.all():
    if self.routecard.open_plan() == self:
        return True


def is_planned(self):
    if self.planned_on:
        return True
    else:
        return False

