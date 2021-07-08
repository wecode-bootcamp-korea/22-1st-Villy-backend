from django.db   import models

from core.models import TimeStampModel

class OrderStatus(models.Model): 
    status = models.CharField(max_length=100)

    class Meta: 
        db_table = 'order_statuses'


class OrderListStatus(models.Model): 
    status = models.CharField(max_length=100)

    class Meta: 
        db_table = 'order_list_statuses'


class Shipment(models.Model): 
    company         = models.CharField(max_length=100)
    tracking_number = models.IntegerField()

    class Meta: 
        db_table = 'shipments'


class Order(TimeStampModel): 
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'orders'


class OrderItem(TimeStampModel): 
    order             = models.ForeignKey('Order', on_delete=models.CASCADE)
    product           = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity          = models.PositiveIntegerField(default=1)
    shipment          = models.OneToOneField('Shipment', on_delete=models.CASCADE)
    order_list_status = models.ForeignKey('OrderListStatus', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'order_items'