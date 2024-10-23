from django.db import models

# Create your models here.

class sellertbl(models.Model):
    sellername=models.CharField(max_length=255)
    sellerage=models.IntegerField()
    sellerphone=models.IntegerField()
    selleremail=models.EmailField()
    sellerpassword=models.CharField(max_length=255)
    approval=models.BooleanField(default=False)

categories=[     
    ('wedding','Wedding cake'),
    ('anniversary','Anniversary cake'),
    ('birthday','Birthday cake'),
    ('others','others')
]  

class producttbl(models.Model):
    cakename=models.CharField(max_length=255)
    cakeprice=models.IntegerField()
    category=models.CharField(max_length=255,choices=categories,default='others')    
    cakeimage=models.FileField(upload_to='cakes')
    quantity=models.IntegerField(default=1)
    selleridFK=models.ForeignKey(sellertbl,on_delete=models.CASCADE,null=True)
