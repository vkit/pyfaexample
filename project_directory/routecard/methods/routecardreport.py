def __str__(self):
    return "{0}sad".format(self.plan.__str__())


def save(self, *args, **kwargs):
    total_accepted = self.production_qty + self.plan.total_accepted_quantity()
    if total_accepted >= self.plan.routecard.quantity:
        self.plan.is_complete = True
        self.plan.save()
    return super(self.__class__, self).save(*args, **kwargs)

