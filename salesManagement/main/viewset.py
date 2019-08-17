from django.shortcuts import get_object_or_404
from .serializer import productSerliz, batchSerliz, salesSerliz, feeprogSerliz, BatchStatusSerliz, StatisticsSerliz
from .models import feeprog, product, batch, sales, currency, BatchStatus, Statistics
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

class statisticsViewset(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerliz
    permission_classes = (permissions.IsAuthenticated,)
    
class salesCustom(APIView):
    """
    Delete sales entry. This will increment the relative batch quantity and cost
    """
    def delete(self, request, orderid):
        print("correct")
        salesObj = get_object_or_404(sales, orderid=orderid)
        try:
            batchObj=batch.objects.get(batchid__exact=salesObj.batchid)
            batchObj.quant=batchObj.quant+1
            batchObj.total_cost=batchObj.total_cost+batchObj.unit_price
            batchObj.save()
        except:
            batchObj=batch()
            batchObj.product_type=salesObj.product_type
            batchObj.quant=salesObj.quant
            batchObj.batchid=str(salesObj.product_type)+"return"
            batchObj.unit_price=salesObj.saleprice-salesObj.unitprofit
            batchObj.minselling=utility.calMinSelling(batchObj.unit_price,request.META["HTTP_FEEPROG"])
            batchObj.currency=currency.objects.get(name__exact='SAR')
            batchObj.total_cost=batchObj.unit_price*batchObj.quant
            batchObj.profit10=utility.calSellingatProfitPercent(batchObj.unit_price,request.META["HTTP_FEEPROG"],0.1)
            batchObj.save()
        salesObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
