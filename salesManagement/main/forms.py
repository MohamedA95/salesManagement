from django import forms
from .models import product, sales, batch, commission,currency
from django.core.validators import MinValueValidator

class productform(forms.Form):
    name = forms.CharField(label="Name")
    product_type = forms.ModelChoiceField(queryset=commission.objects.all(), empty_label=None,label="Type")
    image = forms.ImageField(label="Image",required=False)
    description = forms.CharField(label="Description",required=False)
    def is_valid(self):
        if not super().is_valid():
            return  False
        try:
            pro=product.objects.get(name__exact=self.cleaned_data['name'])
            print("try")
        except:
            print("excapt")
            return True
        return False
class batchform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.all(), empty_label=None,label="Product")
    quant = forms.IntegerField(validators=[MinValueValidator(1)],label="Quantity")
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None,label="Currency",help_text='used to buy the product')
    total_cost = forms.FloatField(validators=[MinValueValidator(1)],label="Total order cost",help_text='In the chosen currency')
    batchid = forms.CharField(label="Batch ID",help_text='Uniqe ID for this batch of products')
    def is_valid(self):
        if not super().is_valid():
            return  False
        try:
            pro=product.objects.get(batchid__exact=self.cleaned_data['batchid'])
            print("try")
        except:
            print("excapt")
            return True
        return False
class salesform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.all(), empty_label=None,label="Product")
    quant=forms.IntegerField(validators=[MinValueValidator(1)],label="Quantity")
    saleprice=forms.FloatField(validators=[MinValueValidator(0)],label="Revenue",help_text='per unit')
    batchid=forms.ModelChoiceField(queryset=batch.objects.filter(quant__gt=0), empty_label=None,label="Batch ID")

class calcform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=commission.objects.all(), empty_label=None,label="Type")
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None,label="Currency",help_text='used to buy the product')
    unit_cost = forms.FloatField(validators=[MinValueValidator(1)],label="Unit Cost",help_text='In the chosen currency')
    local_price=forms.FloatField(validators=[MinValueValidator(0)],label="Unit Cost in local market")
