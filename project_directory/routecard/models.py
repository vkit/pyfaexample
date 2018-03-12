from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp, Contact
import methods




# 
# 	
# 
# 	
# 
# 	
# 

SHIFT = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

RouteCardDict = {
    '__module__': 'routecard',

    'number': models.IntegerField(blank=True),
    'jobspec': models.ForeignKey('jobspec.Jobspec',),

    'quantity': models.IntegerField(default=0,),

    'po_no': models.CharField(max_length=50,),
    'delivery_date': models.DateTimeField(null=True, unique=False,),

}

for name, cls in methods.routecard.__dict__.items():
    if callable(cls):
        RouteCardDict[name] = cls

RouteCard = type(
    str('RouteCard'),
    (TimeStamp,),
    RouteCardDict
)




# 
# 	
# 
# 	
# 
# 	
# 
# 	
# 
# 	
# 
# 	
# 
# 	
# 

RouteCardReportDict = {
    '__module__': 'routecard',

    'shift': models.IntegerField(choices=SHIFT,),

    'production_qty': models.IntegerField(default=0,),

    'rejection_qty': models.IntegerField(default=0,),

    'operator': models.ForeignKey('operators.Operator',),

    'start_time': models.DateTimeField(null=True,unique=False,),

    'end_time': models.DateTimeField(blank=True,null=True,unique=False,),

    'plan': models.ForeignKey('routecard.Plan',null=True,unique=False,related_name="reports",),

}

for name, cls in methods.routecardreport.__dict__.items():
    if callable(cls):
        RouteCardReportDict[name] = cls

RouteCardReport = type(
    str('RouteCardReport'),
    (TimeStamp,),
    RouteCardReportDict
)




# 
# 	
# 
# 	
# 
# 	
# 

PlanDict = {
    '__module__': 'routecard',

    'process': models.ForeignKey('process.Process',),

    'routecard': models.ForeignKey('routecard.Routecard',),

    'machine': models.ForeignKey('machine.Machine',null=True,unique=False,),

    'planned_on': models.DateTimeField(null=True,unique=False, blank=True),

    'is_complete': models.BooleanField(default=False)
}

for name, cls in methods.plan.__dict__.items():
    if callable(cls):
        PlanDict[name] = cls

Plan = type(
    str('Plan'),
    (TimeStamp,),
    PlanDict
)




# 
# 	
# 
# 	
# 

TimeQuantaDict = {
    '__module__': 'routecard',

    'plan': models.ForeignKey('routecard.Plan',null=True,unique=False,related_name="timings",),

    'start_time': models.DateTimeField(null=True,unique=False,),

}

for name, cls in methods.timequanta.__dict__.items():
    if callable(cls):
        TimeQuantaDict[name] = cls

TimeQuanta = type(
    str('TimeQuanta'),
    (TimeStamp,),
    TimeQuantaDict
)

