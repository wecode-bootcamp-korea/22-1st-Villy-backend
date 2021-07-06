from django.db import models

class User(models.Model): 
    email      = models.EmailField()
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=50)
    mobile     = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'users'

class Point(models.Model): 
    user       = models.ForeignKey('User',on_delete=models.CASCADE)
    point      = models.DecimalField(max_digits=10, decimal_places=2)
    history    = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'points'
