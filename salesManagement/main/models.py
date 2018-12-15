from django.db import models

# Create your models here.
class commission(models.Model):
    product_type=models.CharField( primary_key=True,max_length=100,default='',null=False, blank=False)
    multiplyfee=models.FloatField(null=False, blank=False,default=0)
    addfee=models.FloatField(null=False, blank=False,default=0)

class product(models.Model):
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    product_type=models.ForeignKey(commission,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='ProductsImages',blank=True,null=True)
    description=models.CharField(max_length=1000,default='',blank=True,null=True)
class batch(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField()
    unitprice=models.FloatField()
    uid=models.CharField(max_length=100,default='',null=False,blank=False)
    minselling=models.FloatField(default=0)
class sales(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField()
    saleprice=models.FloatField()
    batchid=models.ForeignKey(batch,on_delete=models.SET_DEFAULT,default='')
    profit=models.FloatField()
    time=models.DateField(auto_now=True)
        