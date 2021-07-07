from django.db import models
from timestamp import TimeStampModel


class OrderStatus(models.Model): 
    status = models.CharField(max_length=100)

    class Meta: 
        db_table = 'order_statuses'


class Shipment(models.Model): 
    company         = models.CharField(max_length=100)
    tracking_number = models.IntegerField()

    class Meta: 
        db_table = 'shipments'


class Order(TimeStampModel): 
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100)

    class Meta: 
        db_table = 'orders'


class OrderItem(TimeStampModel): 
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField(default=1)
    order      = models.ForeignKey('Order', on_delete=models.CASCADE)
    shipment   = models.OneToOneField('Shipment', on_delete=models.CASCADE, primary_key=True)

    class Meta: 
        db_table = 'order_items'