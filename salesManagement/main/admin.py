from django.contrib import admin
from .models import currency,product,batch,sales,fee_prog,BatchStatus,Statistics
# Register your models here.
admin.site.register(currency)
admin.site.register(product)
admin.site.register(batch)
admin.site.register(sales)
admin.site.register(fee_prog)
admin.site.register(BatchStatus)
admin.site.register(Statistics)