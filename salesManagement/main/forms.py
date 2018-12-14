from django.forms import ModelForm
from .models import product,sales,batch
class productform(ModelForm):
    class Meta:
        model=product
        fields=['name','product_type','image','description']