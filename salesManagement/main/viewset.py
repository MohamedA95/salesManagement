from .serializer import productSerliz,batchSerliz,salesSerliz,commissionSerliz
from .models import commission,product,batch,sales
from rest_framework import viewsets

class commissionViewSet(viewsets.ModelViewSet):
    queryset=commission.objects.all()
    serializer_class=commissionSerliz

class productViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productSerliz

class batchViewSet(viewsets.ModelViewSet):
    queryset=batch.objects.all()
    serializer_class=batchSerliz

class salesViewSet(viewsets.ModelViewSet):
    queryset=sales.objects.all()
    serializer_class=salesSerliz