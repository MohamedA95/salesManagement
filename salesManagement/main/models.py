from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.conf import settings

class currency(models.Model):
    name=models.CharField(max_length=100,default='USD',unique=True)
    exchange_rate=models.FloatField(blank=False,null=False,default=3.75)
    def __str__(self):
        return self.name
class fee_prog(models.Model):
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    add_fee=models.FloatField(default=0)
    multiply_fee=models.FloatField(default=1)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']        
class BatchStatus(models.Model):
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    cost=models.FloatField(default=0)
    def __str__(self):
        return self.name
class product(models.Model):
    asin=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    product_type=models.CharField(max_length=100,default='',null=True,unique=False, blank=True)
    description=models.CharField(max_length=1000,default='',blank=True,null=True)
    avalible=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']
class batch(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_DEFAULT,default='')
    quant=models.IntegerField(default=0)
    currency=models.ForeignKey(currency,on_delete=models.SET_DEFAULT,default=1)
    unit_price=models.FloatField(default=0.0)
    batch_id=models.CharField(max_length=100,default='',null=False,blank=False,unique=True)
    min_selling=models.FloatField(default=0)
    date=models.DateField(auto_now=True)
    total_cost=models.FloatField(default=0.0)
    profit10=models.FloatField(default=0.0)
    fee_prog=models.ForeignKey(fee_prog,on_delete=models.SET_NULL,null=True)
    date=models.DateField(auto_now=True)
    status=models.ForeignKey(BatchStatus,on_delete=models.SET_DEFAULT,default='')
    def __str__(self):
       return self.batch_id
    class Meta:
        ordering=['quant']

class sales(models.Model):
    product_type=models.ForeignKey(product,on_delete=models.SET_NULL,null=True,default='')
    quant=models.IntegerField()
    sale_price=models.FloatField()
    batch_id=models.ForeignKey(batch,on_delete = models.SET_NULL, null=True, blank=True,limit_choices_to=Q(quant__gt=0))
    unit_profit=models.FloatField(default=0.0)
    profit_percent=models.FloatField(default=0.0)
    total_profit=models.FloatField(default=0.0)
    profit=models.FloatField(default=0.0)
    date=models.DateField(auto_now=True)
    order_id=models.CharField(max_length=200,default='',blank=True,null=True,unique=True)
    class Meta:
        ordering=['-date']
class Statistics(models.Model):
    name=models.CharField(max_length=100,default='',null=False,unique=True, blank=False)
    value=models.FloatField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-name']