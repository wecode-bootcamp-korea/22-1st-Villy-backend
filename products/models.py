from django.db import models

class Product(models.Model): 
    name              = models.CharField(max_length=50)
    description       = models.TextField()
    price             = models.IntegerField()
    dosage            = models.IntegerField()
    details_image_url = models.URLField()
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'products'


class ProductImage(models.Model): 
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url  = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'productsimages'


class ImageType(models.Model): 
    product_image = models.ForeignKey('ProductImage',on_delete=models.CASCADE)
    name          = models.CharField(max_length=50)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'imagestypes'