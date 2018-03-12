def __unicode__(self):
    return "{0}-{1}".format(self.number, self.name)


def total_estimated_time(self):
    time = 0
    for process in self.process_set.all():
        time += (process.estimated_cycle_hours() * self.delivery_qty)
        time += process.estimated_setting_hours()
    return round(time, 2)


def total_processes(self):
    return self.process_set.count()
