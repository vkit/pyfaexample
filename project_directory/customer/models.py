from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp, Contact
import methods




# 

CustomerDict = {
    '__module__': 'customer',

}

for name, cls in methods.customer.__dict__.items():
    if callable(cls):
        CustomerDict[name] = cls

Customer = type(
    str('Customer'),
    (Contact,TimeStamp,),
    CustomerDict
)
