from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.conf import settings
import uuid
# Create your models here.
def filename_generator(pro, _):
    filename = "{}.{}".format(pro.name,str(pro.image).split('.')[-1])
    return 'ProductsImages/'+filename
class currency(models.Model):
    name=models.CharField(primary_key=True,max_length=100,default='USD')
    exrate=models.FloatField(blank=False,null=False,default=3.75)
    def __str__(self):
        return self.name
class commission(models.Model):
    product_type=models.CharField( primary_key=True,max_length=100,default='',null=False, blank=False)
    multiplyfee=models.FloatField(null=False, blank=False,default=0)
    addfee=models.FloatField(null=False, blank=False,default=0)
    def __str__(self):
        return self.product_type

class product(models.Model):
    name=models.CharField(primary_key=True,max_length=100,default='',null=False,unique=True, blank=False)
    product_type=models.ForeignKey(commission,on_delete=models.CASCADE)
    rimage=models.CharField(max_length=1000,default='',blank=True,null=True)
    image=models.ImageField(upload_to=filename_generator,blank=True,null=True,default='')
    description=models.CharField(max_length=1000,default='',blank=True,null=True)
    def __str__(self):
        return self.name
class batch(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField(default=0)
    currency=models.ForeignKey(currency,on_delete=models.SET_DEFAULT,default=1)
    unit_price=models.FloatField(default=0.0)
    batchid=models.CharField(primary_key=True,max_length=100,default='',null=False,blank=False,unique=True)
    minselling=models.FloatField(default=0)
    date=models.DateField(auto_now=True)
    total_cost=models.FloatField(default=0.0)
    def __str__(self):
       return self.batchid

class sales(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_NULL,null=True,default='')
    quant=models.IntegerField()
    saleprice=models.FloatField()
    batchid=models.ForeignKey(batch,on_delete = models.SET_NULL, null=True, blank=True,limit_choices_to=Q(quant__gt=0))
    unitprofit=models.FloatField(default=0.0)
    profitpercent=models.FloatField(default=0.0)
    totalprofit=models.FloatField(default=0.0)
    date=models.DateField(auto_now=True)   

