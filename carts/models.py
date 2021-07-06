from django.db import models

class Cart(models.Model): 
    user     = models.ForeignKey('users.User',on_delete=models.CASCADE)
    product  = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    class Meta: 
        db_table = 'carts'
