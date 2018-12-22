from rest_framework import serializers
from .models import product,batch,sales,commission
class productSerliz(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('name','product_type','rimage','description')

class batchSerliz(serializers.ModelSerializer):
    class Meta:
        model=batch
        fields=('product_type','unit_price','quant','batchid','minselling','total_cost')

class salesSerliz(serializers.ModelSerializer):
    class Meta:
        model=sales
        fields=('product_type','quant','saleprice','unitprofit','profitpercent','totalprofit','date')

class commissionSerliz(serializers.ModelSerializer):
    class Meta:
        model=commission
        fields=('product_type','multiplyfee','addfee')