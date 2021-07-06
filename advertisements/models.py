from django.db import models

class Advertisement(models.Model):
    icon_url = models.CharField(max_length=2000)
    content = models.TextField()
    user_info = models.TextField()

    class Meta: 
        db_table = 'advertisements'
