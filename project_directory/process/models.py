from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp
import methods




# 
# 	
# 

ProcessNameDict = {
    '__module__': 'process',

    'name': models.CharField(max_length=50, unique=True),

}

for name, cls in methods.processname.__dict__.items():
    if callable(cls):
        ProcessNameDict[name] = cls

ProcessName = type(
    str('ProcessName'),
    (TimeStamp,),
    ProcessNameDict
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

ProcessDict = {
    '__module__': 'process',

    'process': models.ForeignKey('process.Processname',),

    'estimated_time': models.DurationField(blank=True,null=True,unique=False,),

    'jobspec': models.ForeignKey('jobspec.Jobspec',null=True,unique=False,),

    'estimated_setting_time': models.DurationField(null=True,unique=False,),

    'remark': models.CharField(max_length=100,blank=True, null=True,),

}

for name, cls in methods.process.__dict__.items():
    if callable(cls):
        ProcessDict[name] = cls

Process = type(
    str('Process'),
    (TimeStamp,),
    ProcessDict
)
