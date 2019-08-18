from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from .forms import productform, batchform, salesform,calcform
from .models import  batch, currency,sales,product,feeprog,BatchStatus,Statistics
from .serializer import productSerliz,batchSerliz,salesSerliz,feeprogSerliz
from . import utility
from django.utils.translation import gettext as _
from datetime import date
import sys
def addpro(request):
    if request.method == "POST":
        form = productform(request.POST,request.FILES)
        if form.is_valid():
            proObj=product()
            proObj.name=form.cleaned_data['name']
            if(request.FILES):
                proObj.image=request.FILES['image']
                proObj.rimage="<img height='20%' width='100%' src='/media/"+"{}.{}".format(proObj.name,str(proObj.image).split('.')[-1])+"'/>"
            else:
                proObj.image=None
                proObj.rimage=''
            proObj.description=form.cleaned_data['description']
            proObj.save()
            messages.info(request, _("Product added successfully!"))
        else:
            messages.error(request, "A product with that name already exists!")
    return render(request, 'addproduct.html', {'form': productform})

def rmit(request):
    if request.method == "POST":
        form = salesform(request.POST)
        if form.is_valid():
            salesObj=sales()
            salesObj.product_type=form.cleaned_data['product_type']
            salesObj.quant=form.cleaned_data['quant']
            salesObj.saleprice=form.cleaned_data['saleprice']
            salesObj.batchid=form.cleaned_data['batchid']
            salesObj.orderid=form.cleaned_data['orderid']
            batchObj = batch.objects.get(batchid__exact=salesObj.batchid)
            if(salesObj.product_type != getattr(batchObj, 'product_type')):
                messages.error(request, _("The product is not in this batch, please choose the correct batch!"))
                return render(request, 'removeitem.html', {'form': salesform})
            batchprice = getattr(batchObj, 'unit_price')
            batchQuant = getattr(batchObj, 'quant')
            if batchQuant > salesObj.quant:
                newquant=batchQuant-salesObj.quant
                batch.objects.filter(batchid__exact=salesObj.batchid).update(quant=newquant)
                batch.objects.filter(batchid__exact=salesObj.batchid).update(total_cost=getattr(batchObj, 'unit_price')*newquant)

            elif batchQuant == salesObj.quant:
                batch.objects.filter(batchid__exact=salesObj.batchid).delete()
                salesObj.batchid=None
                if not batch.objects.filter(product_type__exact=salesObj.product_type).exists():
                    product.objects.filter(name__exact=salesObj.product_type).update(avalible=False)

            else:
                messages.error(request, _("Either the product is not added or the Quantity is larger than the avalible!"))
                return render(request, 'removeitem.html', {'form': salesform})
            salesObj.unitprofit = salesObj.saleprice-batchprice
            salesObj.totalprofit = salesObj.unitprofit*salesObj.quant
            salesObj.profitpercent = (salesObj.unitprofit/salesObj.saleprice)*100
            salesObj.save()
            try:
                utility.editStatistics('capital',salesObj.saleprice*salesObj.quant)
                utility.editStatistics(batchObj.status,-batchprice*salesObj.quant)
                utility.editStatistics('total',salesObj.totalprofit)
            except:
                print("Unexpected error:", sys.exc_info()[0])
            messages.info(request, _("Item removed successfully!"))
        else:
            for e in form.errors:
                messages.error(request, _("ERROR:")+e)
    return render(request, 'removeitem.html', {'form': salesform})

def addit(request):
    if request.method == "POST":
        form = batchform(request.POST)
        if form.is_valid():
            batchObj=batch()
            batchObj.product_type=form.cleaned_data['product_type']
            batchObj.feeprog=form.cleaned_data['feeprog']
            batchObj.quant=form.cleaned_data['quant']
            batchObj.currency=form.cleaned_data['currency']
            batchObj.unit_price=form.cleaned_data['total_cost']/batchObj.quant
            exrate = getattr(currency.objects.get(name__exact=batchObj.currency), 'exrate')
            batchObj.unit_price *= exrate
            batchObj.total_cost=form.cleaned_data['total_cost']*exrate
            batchObj.minselling = utility.calMinSelling(batchObj.unit_price,batchObj.feeprog)
            batchObj.profit10 = utility.calSellingatProfitPercent(batchObj.unit_price,batchObj.feeprog,0.1)
            batchObj.status= form.cleaned_data['status']
            if(form.cleaned_data['batchid']==""):
                batchObj.batchid=str(batchObj.product_type)
                batchObj.batchid+=" Q"+str(batchObj.quant)+" "+str(batchObj.unit_price)+" "+date.today().strftime("%d %b")
            else:
                batchObj.batchid=form.cleaned_data['batchid']
            batchObj.save()
            product.objects.filter(name__exact=form.cleaned_data['product_type']).update(avalible=True)
            utility.editStatistics('capital',-batchObj.total_cost)
            try:
                utility.editStatistics(batchObj.status,batchObj.total_cost)
            except:
                utility.createStatistics(batchObj.status,batchObj.total_cost)
            messages.info(request, _("Item added successfully!"))
        else:
            for e in form.errors:
                messages.error(request, "ERROR:"+e)
    return render(request, 'additem.html', {'form': batchform})

def repsales(request):
    return render(request, 'repsales.html')

def repproducts(request):
    return render(request, 'repproducts.html')

def repbatches(request):
    return render(request, 'repbatches.html',{'batchStatus':utility.querysetToJSlist(BatchStatus.objects.all())}) #since we have a small number of status, this should not be heavy on RAM

def repstatistics(request):
    return render(request, 'repstatistics.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return redirect('/accounts/login/')

def calc(request):
    if request.method=="POST":
        form=calcform(request.POST)
        if form.is_valid() :
            fee_prog = feeprog.objects.get(name__exact=form.cleaned_data['feeprog'])
            exrate = getattr(currency.objects.get(name__exact=form.cleaned_data['currency']), 'exrate')
            localprice=form.cleaned_data['local_price']
            onlineprice=float(form.cleaned_data['unit_cost'])*exrate
            minselling = utility.calMinSelling(onlineprice,fee_prog)
            messages.info(request, _("Min selling price is ")+str(minselling)+_(" The diff between Min selling and Local price: ")+str(localprice-minselling))
            messages.info(request,_("Profit percent at local price: ")+str(utility.calProfitPercent(onlineprice,fee_prog,localprice)))
    return render(request, 'calc.html', {'form': calcform})

def getBatchesForProduct(request,product):
    batches=batch.objects.filter(product_type__exact=product,status__in=['FBS','Stock'])
    return render(request,'batchesforproduct.html',{'batches':batches})

def rmsaleorder(request):
    feeprogs=feeprog.objects.all()
    statuss=BatchStatus.objects.all()
    return render(request,'removesaleorder.html',{'feeprogs':feeprogs,'statuss':statuss})

def changeBatchStatus(request):
    batchObj=batch.objects.get(batchid__exact=request.META["HTTP_BATCHID"])
    utility.editStatistics(batchObj.status,-batchObj.total_cost)
    batchObj.status=BatchStatus.objects.get(name__exact=request.META["HTTP_NEWVAL"])
    utility.editStatistics(batchObj.status,batchObj.total_cost)
    batchObj.save()
    return redirect('/rep/batches')

def editCompanyCapital(request):
    utility.newValueStatistics('capital',float(request.META["HTTP_NEWVAL"]))
    temp={}
    totalStat=Statistics.objects.get(name__exact='total')
    totalStat.value=float(request.META["HTTP_NEWVAL"])
    for i in batch.objects.values('status','total_cost'):
        temp[i['status']]=temp.get(i['status'],0)+i['total_cost']
    for i in temp:
        tStat=None
        try:
            tStat=Statistics.objects.get(name__exact=i)
        except:
            tStat=Statistics()
            tStat.name=i
        tStat.value=float(temp[i])
        totalStat.value+=tStat.value
        tStat.save()
    totalStat.save()

    return redirect('/rep/statistics/')