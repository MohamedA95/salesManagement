from django import forms
from .models import Product, Sales, Batch, Currency,FeeProgram,BatchStatus
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy


class productform(forms.Form):
    name = forms.CharField(label=gettext_lazy("Name"))
    description = forms.CharField(label=gettext_lazy("Description"),required=False)
    unique_id = forms.CharField(label=gettext_lazy("Unique ID"),required=True,help_text=gettext_lazy('ASIN or SKU'))
    def is_valid(self):
        if not super().is_valid():
            return  False
        if Product.objects.filter(name__exact=self.cleaned_data['name']).exists():
            return False
        if Product.objects.filter(unique_id__exact=self.cleaned_data['unique_id']).exists():
            return False
        return True
class batchform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None,label=gettext_lazy("Product"))
    quant = forms.IntegerField(validators=[MinValueValidator(1)],label=gettext_lazy("Quantity"))
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), empty_label=None,label=gettext_lazy("Currency"),help_text=gettext_lazy('used to buy the product'))
    total_cost = forms.FloatField(validators=[MinValueValidator(1)],label=gettext_lazy("Total order cost"),help_text=gettext_lazy('In the chosen currency'))
    batch_id = forms.CharField(label=gettext_lazy("Batch ID"),help_text=gettext_lazy('Uniqe ID for this batch of products'),required=False)
    fee_prog=forms.ModelChoiceField(queryset=FeeProgram.objects.all(), empty_label=None,label=gettext_lazy("Fee Prog"))
    status=forms.ModelChoiceField(queryset=BatchStatus.objects.all(), empty_label=None,label=gettext_lazy("Status"))
    
    def is_valid(self):
        if not super().is_valid():
            return  False
        if Batch.objects.filter(batch_id__exact=self.cleaned_data['batch_id']).exists():
            return False
        return True
        
class salesform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=Product.objects.filter(avalible__exact=True), empty_label=None,label=gettext_lazy("Product"))
    quant=forms.IntegerField(validators=[MinValueValidator(1)],label=gettext_lazy("Quantity"),initial=1)
    sale_price=forms.FloatField(validators=[MinValueValidator(0)],label=gettext_lazy("Revenue"))
    sale_price_type=forms.BooleanField(required=False,label=gettext_lazy("Per unit"),help_text=gettext_lazy('Check this is the revenue is per unit'))
    batch_id=forms.ModelChoiceField(queryset=Batch.objects.filter(quant__gt=0), empty_label=None,label=gettext_lazy("Batch ID"))
    order_id=forms.CharField(label=gettext_lazy("Order ID"),help_text=gettext_lazy('Uniqe ID for this order'))


class calcform(forms.Form):
    fee_prog = forms.ModelChoiceField(queryset=FeeProgram.objects.all(), empty_label=None,label=gettext_lazy("Fee Prog"))
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), empty_label=None,label=gettext_lazy("Currency"),help_text=gettext_lazy('used to buy the product'))
    unit_cost = forms.FloatField(validators=[MinValueValidator(1)],label=gettext_lazy("Unit Cost"),help_text=gettext_lazy('In the chosen currency'))
    local_price=forms.FloatField(validators=[MinValueValidator(0)],label=gettext_lazy("Unit Cost in local market"))
