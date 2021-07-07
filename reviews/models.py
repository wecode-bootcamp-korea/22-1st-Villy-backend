from django.db import models
from timestamp import TimeStampModel

class Review(TimeStampModel): 
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    content    = models.TextField()

    class Meta: 
        db_table = 'reviews'