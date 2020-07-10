from rest_framework import serializers
from .models import Product,Batch,Sales,FeeProgram,BatchStatus,Statistics
class productSerliz(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('name','description','avalible')

class batchSerliz(serializers.ModelSerializer):
    class Meta:
        model=Batch
        lookup_field='batch_id'
        fields=('product_type','unit_price','quant','batch_id','min_selling','total_cost','profit10','fee_prog','date','status')

class salesSerliz(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields=('product_type','quant','sale_price','unit_profit','profit_percent','total_profit','date','order_id','batch_id')

class fee_progSerliz(serializers.ModelSerializer):
    class Meta:
        model=FeeProgram
        fields=('name','add_fee','multiply_fee')

class BatchStatusSerliz(serializers.ModelSerializer):
    class Meta:
        model=BatchStatus
        fields=('name')
class StatisticsSerliz(serializers.ModelSerializer):
    class Meta:
        model=Statistics
        fields=('name','value')