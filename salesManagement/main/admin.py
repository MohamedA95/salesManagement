from django.contrib import admin
from .models import commission,currency,product,batch,sales
# Register your models here.
admin.site.register(commission)
admin.site.register(currency)
admin.site.register(product)
admin.site.register(batch)
admin.site.register(sales)