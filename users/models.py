from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel): 
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=50)
    mobile     = models.CharField(max_length=50, unique=True)

    class Meta: 
        db_table = 'users'


class Point(TimeStampModel): 
    user    = models.ForeignKey('User', on_delete=models.CASCADE)
    point   = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta: 
        db_table = 'points'


class PointHistory(TimeStampModel):
    point = models.ForeignKey('Point', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)

    class Meta:
        db_table = 'point_histories'