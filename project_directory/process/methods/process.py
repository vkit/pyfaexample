def __str__(self):
    return "{0}-{1}".format(self.jobspec, self.process)


def estimated_cycle_hours(self):
    if self.estimated_time.total_seconds() is not None:
        return self.estimated_time.total_seconds() / 3600


def estimated_setting_hours(self):
    if self.estimated_setting_time.total_seconds() is not None:
        return self.estimated_setting_time.total_seconds() / 3600

