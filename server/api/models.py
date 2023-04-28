from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100) #from max goodridge tutorial
    description = models.CharField(max_length=500) #from maxgoodrige tutorial