from django.contrib import admin
from .models import currency,product,batch,sales,feeprog,BatchStatus,Statistics
# Register your models here.
admin.site.register(currency)
admin.site.register(product)
admin.site.register(batch)
admin.site.register(sales)
admin.site.register(feeprog)
admin.site.register(BatchStatus)
admin.site.register(Statistics)