from django.db import models

# Create your models here.
class currency(models.Model):
    name=models.CharField(primary_key=True,max_length=100,default='USD')
    exrate=models.FloatField(blank=False,null=False,default=3.75)
class commission(models.Model):
    product_type=models.CharField( primary_key=True,max_length=100,default='',null=False, blank=False)
    multiplyfee=models.FloatField(null=False, blank=False,default=0)
    addfee=models.FloatField(null=False, blank=False,default=0)

class product(models.Model):
    name=models.CharField(primary_key=True,max_length=100,default='',null=False,unique=True, blank=False)
    product_type=models.ForeignKey(commission,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='ProductsImages',blank=True,null=True)
    description=models.CharField(max_length=1000,default='',blank=True,null=True)
class batch(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField(default=0)
    currency=models.ForeignKey(currency,on_delete=models.SET_DEFAULT,default=1)
    unit_price=models.FloatField(default=0.0)
    batchid=models.CharField(primary_key=True,max_length=100,default='',null=False,blank=False,unique=True)
    minselling=models.FloatField(default=0)
class sales(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField()
    saleprice=models.FloatField()
    batchid=models.ForeignKey(batch,on_delete=models.SET_DEFAULT,default='')
    unitprofit=models.FloatField(default=0.0)
    totalprofit=models.FloatField(default=0.0)
    time=models.DateField(auto_now=True)   

