from django.db import models

# Create your models here. 
class Destination(models.Model):
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer  = models.BooleanField(default=False)
    
    
