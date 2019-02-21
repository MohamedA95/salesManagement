from django.contrib import admin
from .models import currency,product,batch,sales,feeprog
# Register your models here.
admin.site.register(currency)
admin.site.register(product)
admin.site.register(batch)
admin.site.register(sales)
admin.site.register(feeprog)