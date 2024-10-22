from django.db import models
from sellerapp.models import producttbl

# Create your models here.

class customertbl(models.Model):       #class objs will the rows of db table
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    place=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)

class carttbl(models.Model):
    customer=models.ForeignKey(customertbl,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(producttbl,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)

class wishlistbl(models.Model):
    customer=models.ForeignKey(customertbl,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(producttbl,on_delete=models.CASCADE,null=True,blank=True)

