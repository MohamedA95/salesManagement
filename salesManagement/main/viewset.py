from django.shortcuts import get_object_or_404
from .serializer import productSerliz, batchSerliz, salesSerliz, fee_progSerliz, BatchStatusSerliz, StatisticsSerliz
from .models import fee_prog, product, batch, sales, currency, BatchStatus, Statistics
from rest_framework import viewsets, status, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from . import utility

class fee_progViewSet(viewsets.ModelViewSet):
    queryset = fee_prog.objects.all()
    serializer_class = fee_progSerliz
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
    lookup_field = 'order_id'

class statisticsViewset(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerliz
    permission_classes = (permissions.IsAuthenticated,)
    
class salesCustom(APIView):
    """
    Delete sales entry. This will increment the relative batch quantity and cost
    """
    def delete(self, request, order_id):
        salesObj = get_object_or_404(sales, order_id=order_id)
        batchstatus=None
        try:
            batchObj=batch.objects.get(batch_id__exact=salesObj.batch_id)
            batchObj.quant=batchObj.quant+1
            batchObj.total_cost=batchObj.total_cost+batchObj.unit_price
            batchstatus=batchObj.status
            batchObj.save()
        except:
            batchObj=batch()
            batchObj.product_type=salesObj.product_type
            batchObj.quant=salesObj.quant
            batchObj.batch_id=str(salesObj.product_type)+"return"
            batchObj.unit_price=salesObj.sale_price-salesObj.unit_profit
            batchObj.min_selling=utility.calcultate_min_selling(batchObj.unit_price,request.META["HTTP_fee_prog"])
            batchObj.currency=currency.objects.get(name__exact='SAR')
            batchObj.total_cost=batchObj.unit_price*batchObj.quant
            batchObj.profit10=utility.calculate_selling_profit_percent(batchObj.unit_price,request.META["HTTP_fee_prog"],0.1)
            batchObj.status=batch.objects.get(name__exact=request.META["HTTP_STATUS"])
            batchstatus=batchObj.status
            batchObj.save()
        utility.edit_statistics('total',-salesObj.total_profit)
        utility.edit_statistics('capital',-salesObj.sale_price*salesObj.quant)
        utility.edit_statistics(batchstatus,batchObj.unit_price*salesObj.quant)
        salesObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
