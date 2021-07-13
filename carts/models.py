from django.db import models

from core.models import TimeStampModel

class Cart(models.Model): 
    user     = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product  = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta: 
        db_table = 'carts'
