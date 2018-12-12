from django.db import models

# Create your models here.
class commission(models.Model):
    typestr=models.CharField(max_length=100,default='',null=False, blank=False)
    saleprice=models.FloatField()
class product(models.Model):
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    typestr=models.ForeignKey(commission,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='ProductsImages',blank=True)
    description=models.CharField(max_length=1000,default='')

class batch(models.Model):
    productname=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField()
    unitprice=models.FloatField()
    uid=models.CharField(max_length=100,default='',null=False,blank=False)
class sales(models.Model):
    productname=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField()
    saleprice=models.FloatField()
    batchid=models.ForeignKey(batch,on_delete=models.SET_DEFAULT,default='')
    profit=models.FloatField()
        