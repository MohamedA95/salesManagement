from .serializer import productSerliz,batchSerliz,salesSerliz,feeprogSerliz
from .models import feeprog,product,batch,sales
from rest_framework import viewsets
from rest_framework import permissions

class feeprogViewSet(viewsets.ModelViewSet):
    queryset=feeprog.objects.all()
    serializer_class=feeprogSerliz
    # permission_classes = (permissions.IsAuthenticated,)

class productViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productSerliz
    # permission_classes = (permissions.IsAuthenticated,)

class batchViewSet(viewsets.ModelViewSet):
    queryset=batch.objects.all()
    serializer_class=batchSerliz
    # permission_classes = (permissions.IsAuthenticated,)

class salesViewSet(viewsets.ModelViewSet):
    queryset=sales.objects.all()
    serializer_class=salesSerliz
    # permission_classes = (permissions.IsAuthenticated,)
