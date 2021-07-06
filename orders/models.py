from django.db import models

class OrderStatus(models.Model): 
    status = models.CharField(max_length=100)

    class Meta: 
        db_table = 'orderstatuses'

class Shipment(models.Model): 
    company         = models.CharField(max_length=100)
    tracking_number = models.IntegerField()

    class Meta: 
        db_table = 'shipments'


class Order(models.Model): 
    user         = models.ForeignKey('users.User',on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus',on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'orders'


class OrderItem(models.Model): 
    product    = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    quantity   = models.IntegerField()
    order      = models.ForeignKey('Order',on_delete=models.CASCADE)
    shipment   = models.ForeignKey('Shipment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'orderitems'


