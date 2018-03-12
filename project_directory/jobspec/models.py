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
# 	
# 

JobSpecDict = {
    '__module__': 'jobspec',

    'number': models.CharField(max_length=15,unique=True,verbose_name=("Parts No")),

    'customer': models.ForeignKey('customer.Customer',),

    'name': models.CharField(max_length=50,verbose_name=("Parts Name")),

    'delivery_qty': models.IntegerField(default=0,),

}

for name, cls in methods.jobspec.__dict__.items():
    if callable(cls):
        JobSpecDict[name] = cls

JobSpec = type(
    str('JobSpec'),
    (TimeStamp,),
    JobSpecDict
)

