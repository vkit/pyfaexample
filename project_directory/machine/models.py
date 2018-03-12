from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp, Contact
import methods




# 
# 	
# 
# 	
# 

MachineDict = {
    '__module__': 'machine',

    'name': models.CharField(max_length=50, unique=True),

}

for name, cls in methods.machine.__dict__.items():
    if callable(cls):
        MachineDict[name] = cls

Machine = type(
    str('Machine'),
    (TimeStamp,),
    MachineDict
)

