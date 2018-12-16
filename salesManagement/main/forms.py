from django.forms import ModelForm
from .models import product,sales,batch
class productform(ModelForm):
    class Meta:
        model=product
        fields=['name','product_type','image','description']

class batchform(ModelForm):
    class Meta:
        model=batch
        fields=['product_type','unit_price','quant','uid']

class salesform(ModelForm):
    class Meta:
        model=sales
        fields=['product_type','batchid','quant','saleprice']