from rest_framework import serializers
from .models import product,batch,sales,feeprog,BatchStatus,Statistics
class productSerliz(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('name','rimage','description','avalible')

class batchSerliz(serializers.ModelSerializer):
    class Meta:
        model=batch
        lookup_field='batchid'
        fields=('product_type','unit_price','quant','batchid','minselling','total_cost','profit10','feeprog','date','status')

class salesSerliz(serializers.ModelSerializer):
    class Meta:
        model=sales
        fields=('product_type','quant','saleprice','unitprofit','profitpercent','totalprofit','date','orderid','batchid')

class feeprogSerliz(serializers.ModelSerializer):
    class Meta:
        model=feeprog
        fields=('name','addfee','mulfee')

class BatchStatusSerliz(serializers.ModelSerializer):
    class Meta:
        model=BatchStatus
        fields=('name')
class StatisticsSerliz(serializers.ModelSerializer):
    class Meta:
        model=Statistics
        fields=('name','value')