from django.contrib import admin
from .models import Currency,Product,Batch,Sales,FeeProgram,BatchStatus,Statistics
# Register your models here.
admin.site.register(Currency)
admin.site.register(Product)
admin.site.register(Batch)
admin.site.register(Sales)
admin.site.register(FeeProgram)
admin.site.register(BatchStatus)
admin.site.register(Statistics)