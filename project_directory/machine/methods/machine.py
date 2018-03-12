from django.utils import timezone


def __str__(self):
    return self.name


def schedule_list(self):
    plans = self.plan_set.all()
    schedule_list = [[plan.formated_time(), plan.formated_end_time()] for plan in plans if plan.formated_time() is not None]
    schedule_list = str(schedule_list)
    schedule_list = schedule_list.replace("'", "")
    return schedule_list


def total_process_count(self):
    return self.plan_set.count()


def check_availability(self, date):
    plans = self.plan_set.all()
    from dateutil.parser import parse
    date = parse(str(date))
    for plan in plans:
        if plan.planned_on:
            if plan.planned_on <= date <= plan.end_time():
                return False
    return True
