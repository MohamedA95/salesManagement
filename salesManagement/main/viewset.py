from .serializer import productSerliz,batchSerliz,salesSerliz,commissionSerliz
from .models import commission,product,batch,sales
from rest_framework import viewsets
from rest_framework import permissions

class commissionViewSet(viewsets.ModelViewSet):
    queryset=commission.objects.all()
    serializer_class=commissionSerliz
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class productViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productSerliz
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class batchViewSet(viewsets.ModelViewSet):
    queryset=batch.objects.all()
    serializer_class=batchSerliz
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class salesViewSet(viewsets.ModelViewSet):
    queryset=sales.objects.all()
    serializer_class=salesSerliz
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
