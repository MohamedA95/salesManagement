from rest_framework import serializers
from .models import product,batch,sales,fee_prog,BatchStatus,Statistics
class productSerliz(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('name','image_path','description','avalible')

class batchSerliz(serializers.ModelSerializer):
    class Meta:
        model=batch
        lookup_field='batch_id'
        fields=('product_type','unit_price','quant','batch_id','min_selling','total_cost','profit10','fee_prog','date','status')

class salesSerliz(serializers.ModelSerializer):
    class Meta:
        model=sales
        fields=('product_type','quant','sale_price','unit_profit','profit_percent','total_profit','date','order_id','batch_id')

class fee_progSerliz(serializers.ModelSerializer):
    class Meta:
        model=fee_prog
        fields=('name','add_fee','multiply_fee')

class BatchStatusSerliz(serializers.ModelSerializer):
    class Meta:
        model=BatchStatus
        fields=('name')
class StatisticsSerliz(serializers.ModelSerializer):
    class Meta:
        model=Statistics
        fields=('name','value')