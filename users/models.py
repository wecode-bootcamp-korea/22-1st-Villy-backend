from django.db import models
from timestamp import TimeStampModel

class User(TimeStampModel): 
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=50, unique=True)
    mobile     = models.CharField(max_length=50, unique=True)

    class Meta: 
        db_table = 'users'

class Point(TimeStampModel): 
    user       = models.ForeignKey('User', on_delete=models.CASCADE)
    point      = models.DecimalField(max_digits=10, decimal_places=2)
    history    = models.CharField(max_length=200)

    class Meta: 
        db_table = 'points'