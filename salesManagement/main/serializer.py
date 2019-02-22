from rest_framework import serializers
from .models import product,batch,sales,feeprog
class productSerliz(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('name','rimage','description')

class batchSerliz(serializers.ModelSerializer):
    class Meta:
        model=batch
        fields=('product_type','unit_price','quant','batchid','minselling','total_cost','profit10','feeprog')

class salesSerliz(serializers.ModelSerializer):
    class Meta:
        model=sales
        fields=('product_type','quant','saleprice','unitprofit','profitpercent','totalprofit','date')

class feeprogSerliz(serializers.ModelSerializer):
    class Meta:
        model=feeprog
        fields=('name','addfee','mulfee')