from django import forms
from .models import product, sales, batch, currency,feeprog,BatchStatus
from django.core.validators import MinValueValidator
from django.utils.translation import gettext as _


class productform(forms.Form):
    name = forms.CharField(label=_("Name"))
    image = forms.ImageField(label=_("Image"),required=False)
    description = forms.CharField(label=_("Description"),required=False)
    def is_valid(self):
        if not super().is_valid():
            return  False
        if product.objects.filter(name__exact=self.cleaned_data['name']).exists():
            return False
        return True
class batchform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.all(), empty_label=None,label=_("Product"))
    quant = forms.IntegerField(validators=[MinValueValidator(1)],label=_("Quantity"))
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None,label=_("Currency"),help_text=_('used to buy the product'))
    total_cost = forms.FloatField(validators=[MinValueValidator(1)],label=_("Total order cost"),help_text=_('In the chosen currency'))
    batchid = forms.CharField(label=_("Batch ID"),help_text=_('Uniqe ID for this batch of products'),required=False)
    feeprog=forms.ModelChoiceField(queryset=feeprog.objects.all(), empty_label=None,label=_("Fee Prog"))
    status=forms.ModelChoiceField(queryset=BatchStatus.objects.all(), empty_label=None,label=_("Status"))
    
    def is_valid(self):
        if not super().is_valid():
            return  False
        if batch.objects.filter(batchid__exact=self.cleaned_data['batchid']).exists():
            return False
        return True
        
class salesform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.filter(avalible__exact=True), empty_label=None,label=_("Product"))
    quant=forms.IntegerField(validators=[MinValueValidator(1)],label=_("Quantity"))
    saleprice=forms.FloatField(validators=[MinValueValidator(0)],label=_("Revenue"),help_text=_('per unit'))
    batchid=forms.ModelChoiceField(queryset=batch.objects.filter(quant__gt=0), empty_label=None,label=_("Batch ID"))
    orderid=forms.CharField(label=_("Order ID"),help_text=_('Uniqe ID for this order'))

class calcform(forms.Form):
    feeprog = forms.ModelChoiceField(queryset=feeprog.objects.all(), empty_label=None,label=_("Fee Prog"))
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None,label=_("Currency"),help_text=_('used to buy the product'))
    unit_cost = forms.FloatField(validators=[MinValueValidator(1)],label=_("Unit Cost"),help_text=_('In the chosen currency'))
    local_price=forms.FloatField(validators=[MinValueValidator(0)],label=_("Unit Cost in local market"))
