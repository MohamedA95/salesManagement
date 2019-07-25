from django.shortcuts import get_object_or_404
from .serializer import productSerliz, batchSerliz, salesSerliz, feeprogSerliz
from .models import feeprog, product, batch, sales
from rest_framework import viewsets, status, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from . import utility

class feeprogViewSet(viewsets.ModelViewSet):
    queryset = feeprog.objects.all()
    serializer_class = feeprogSerliz
    permission_classes = (permissions.IsAuthenticated,)


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerliz
    permission_classes = (permissions.IsAuthenticated,)


class batchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = batch.objects.all()
    serializer_class = batchSerliz


class salesViewSet(viewsets.ModelViewSet):
    queryset = sales.objects.all()
    serializer_class = salesSerliz
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'orderid'

    def destroy(self, request, orderid=None):
        print(orderid)
        salesObj = get_object_or_404(sales, orderid=orderid)
        print(salesObj.product_type)
        print(salesObj.quant)
        print(salesObj.saleprice)
        print(salesObj.batchid)
        print(salesObj.unitprofit)
        print(salesObj.orderid)
        try:
            batchObj=batch.objects.get(batchid__exact=salesObj.batchid)
            batchObj.quant=batchObj.quant+1
            batchObj.total_cost=batchObj.total_cost+batchObj.unit_price
            batchObj.save()
        except:
            batchObj=batch()
            batchObj.product_type=salesObj.product_type
            batchObj.quant=1
            batchObj.batchid='return'+str(salesObj.product_type)
            batchObj.unit_price=((salesObj.profitpercent/100)-1)*salesObj.unitprofit
            batchObj.minselling=utility.calMinSelling(batchObj.unit_price,batchObj.feeprog)
            batchObj.profit10 = utility.calProfitPercent(batchObj.unit_price,batchObj.feeprog,0.1)
            batchObj.save()
        salesObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class salesCustom(APIView):
    """
    Delete sales entry. This will increment the relative batch quantity and cost
    """
    # def get(self, request, batchid):
    #     batcho = get_object_or_404(batch,batchid=batchid)
    #     serializer = batchSerliz(batcho)
    #     return Response(serializer.data)

    def delete(self, request, orderid):
        print(orderid)
        salesObj = get_object_or_404(sales, orderid=orderid)
        print(salesObj.product_type)
        print(salesObj.quant)
        print(salesObj.saleprice)
        print(salesObj.batchid)
        print(salesObj.unitprofit)
        print(salesObj.orderid)
        try:
            batchObj=batch.objects.get(batchid__exact=salesObj.batchid)
            batchObj.quant=batchObj.quant+1
            batchObj.total_cost=batchObj.total_cost+batchObj.unit_price
        except:
            batchObj=batch()
            batchObj.product_type=salesObj.product_type
            batchObj.quant=1
            batchObj.batchid=salesObj.batchid
            # batchObj.minselling=
        print(batchObj.minselling)
        return Response(status=status.HTTP_204_NO_CONTENT)
