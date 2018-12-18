from django import forms
from .models import product, sales, batch, commission,currency

class productform(forms.Form):
    name = forms.CharField()
    product_type = forms.ModelChoiceField(queryset=commission.objects.all(), empty_label=None)
    image = forms.ImageField()
    description = forms.CharField()


class batchform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.all(), empty_label=None)
    quant = forms.IntegerField()
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None)
    unit_price = forms.FloatField()
    batchid = forms.CharField()

class salesform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.all(), empty_label=None)
    quant=forms.IntegerField()
    saleprice=forms.FloatField()
    batchid=forms.ModelChoiceField(queryset=batch.objects.filter(quant__gt=0), empty_label=None)