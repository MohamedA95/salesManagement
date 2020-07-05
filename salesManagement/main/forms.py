from django import forms
from .models import product, sales, batch, currency,fee_prog,BatchStatus
from django.core.validators import MinValueValidator
from django.utils.translation import gettext as _


class productform(forms.Form):
    name = forms.CharField(label=_("Name"))
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
    batch_id = forms.CharField(label=_("Batch ID"),help_text=_('Uniqe ID for this batch of products'),required=False)
    fee_prog=forms.ModelChoiceField(queryset=fee_prog.objects.all(), empty_label=None,label=_("Fee Prog"))
    status=forms.ModelChoiceField(queryset=BatchStatus.objects.all(), empty_label=None,label=_("Status"))
    
    def is_valid(self):
        if not super().is_valid():
            return  False
        if batch.objects.filter(batch_id__exact=self.cleaned_data['batch_id']).exists():
            return False
        return True
        
class salesform(forms.Form):
    product_type = forms.ModelChoiceField(queryset=product.objects.filter(avalible__exact=True), empty_label=None,label=_("Product"))
    quant=forms.IntegerField(validators=[MinValueValidator(1)],label=_("Quantity"),initial=1)
    sale_price=forms.FloatField(validators=[MinValueValidator(0)],label=_("Revenue"),help_text=_('per unit'))
    batch_id=forms.ModelChoiceField(queryset=batch.objects.filter(quant__gt=0), empty_label=None,label=_("Batch ID"))
    order_id=forms.CharField(label=_("Order ID"),help_text=_('Uniqe ID for this order'))

class calcform(forms.Form):
    fee_prog = forms.ModelChoiceField(queryset=fee_prog.objects.all(), empty_label=None,label=_("Fee Prog"))
    currency = forms.ModelChoiceField(queryset=currency.objects.all(), empty_label=None,label=_("Currency"),help_text=_('used to buy the product'))
    unit_cost = forms.FloatField(validators=[MinValueValidator(1)],label=_("Unit Cost"),help_text=_('In the chosen currency'))
    local_price=forms.FloatField(validators=[MinValueValidator(0)],label=_("Unit Cost in local market"))
