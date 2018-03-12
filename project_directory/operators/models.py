from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp, Contact
import methods




# 
# 	
# 

OperatorDict = {
    '__module__': 'operators',

    'name': models.CharField(max_length=50,),

}

for name, cls in methods.operator.__dict__.items():
    if callable(cls):
        OperatorDict[name] = cls

Operator = type(
    str('Operator'),
    (TimeStamp,),
    OperatorDict
)

