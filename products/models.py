from django.db   import models

from core.models import TimeStampModel

class Product(TimeStampModel): 
    name                = models.CharField(max_length=50)
    description         = models.TextField()
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    tablet              = models.IntegerField()
    thumbnail_image_url = models.URLField()

    class Meta: 
        db_table = 'products'


class ProductIcon(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    icon    = models.URLField()
    name    = models.CharField(max_length=10)

    class Meta:
        db_table = 'product_icons'


class ProductSummary(models.Model):
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)
    summary   = models.CharField(max_length=50)

    class Meta: 
        db_table = 'product_summaries'
