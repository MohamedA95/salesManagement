from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from .forms import productform, batchform, salesform,calcform
from .models import  batch, currency,sales,product,fee_prog,BatchStatus,Statistics
from .serializer import productSerliz,batchSerliz,salesSerliz,fee_progSerliz
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
                proObj.image_path="<img height='20%' width='100%' src='/media/"+"{}.{}".format(proObj.name,str(proObj.image).split('.')[-1])+"'/>"
                print(proObj.image)
                print(proObj.image_path)
            else:
                proObj.image=None
                proObj.image_path=''
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
            salesObj.sale_price=form.cleaned_data['sale_price']
            salesObj.batch_id=form.cleaned_data['batch_id']
            if(sales.objects.filter(order_id__exact=form.cleaned_data['order_id']).count()!=0):
                messages.error(request, _("This order is already registered!"))
                return render(request, 'removeitem.html', {'form': salesform})
            salesObj.order_id=form.cleaned_data['order_id']
            batchObj = batch.objects.get(batch_id__exact=salesObj.batch_id)
            if(salesObj.product_type != getattr(batchObj, 'product_type')):
                messages.error(request, _("The product is not in this batch, please choose the correct batch!"))
                return render(request, 'removeitem.html', {'form': salesform})
            batchprice = getattr(batchObj, 'unit_price')
            batchQuant = getattr(batchObj, 'quant')
            if batchQuant > salesObj.quant:
                newquant=batchQuant-salesObj.quant
                batch.objects.filter(batch_id__exact=salesObj.batch_id).update(quant=newquant)
                batch.objects.filter(batch_id__exact=salesObj.batch_id).update(total_cost=getattr(batchObj, 'unit_price')*newquant)

            elif batchQuant == salesObj.quant:
                batch.objects.filter(batch_id__exact=salesObj.batch_id).delete()
                salesObj.batch_id=None
                if not batch.objects.filter(product_type__exact=salesObj.product_type).exists():
                    product.objects.filter(name__exact=salesObj.product_type).update(avalible=False)

            else:
                messages.error(request, _("Either the product is not added or the Quantity is larger than the avalible!"))
                return render(request, 'removeitem.html', {'form': salesform})
            salesObj.unit_profit = salesObj.sale_price-batchprice
            salesObj.total_profit = salesObj.unit_profit*salesObj.quant
            salesObj.profit_percent = (salesObj.unit_profit/salesObj.sale_price)*100
            salesObj.save()
            try:
                utility.edit_statistics('capital',salesObj.sale_price*salesObj.quant)
                utility.edit_statistics(batchObj.status,-batchprice*salesObj.quant)
                utility.edit_statistics('total',salesObj.total_profit)
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
            batchObj.fee_prog=form.cleaned_data['fee_prog']
            batchObj.quant=form.cleaned_data['quant']
            batchObj.currency=form.cleaned_data['currency']
            batchObj.unit_price=form.cleaned_data['total_cost']/batchObj.quant
            exchange_rate = getattr(currency.objects.get(name__exact=batchObj.currency), 'exchange_rate')
            batchObj.unit_price *= exchange_rate
            batchObj.total_cost=form.cleaned_data['total_cost']*exchange_rate
            batchObj.min_selling = utility.calcultate_min_selling(batchObj.unit_price,batchObj.fee_prog)
            batchObj.profit10 = utility.calculate_selling_profit_percent(batchObj.unit_price,batchObj.fee_prog,0.1)
            batchObj.status= form.cleaned_data['status']
            if(form.cleaned_data['batch_id']==""):
                batchObj.batch_id=str(batchObj.product_type)
                batchObj.batch_id+=" Q"+str(batchObj.quant)+" "+str(round(batchObj.unit_price,2))+" "+date.today().strftime("%d %b")
            else:
                batchObj.batch_id=form.cleaned_data['batch_id']
            batchObj.save()
            product.objects.filter(name__exact=form.cleaned_data['product_type']).update(avalible=True)
            utility.edit_statistics('capital',-batchObj.total_cost)
            try:
                utility.edit_statistics(batchObj.status,batchObj.total_cost)
            except:
                utility.create_statistics(batchObj.status,batchObj.total_cost)
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
    return render(request, 'repbatches.html',{'batchStatus':utility.queryset_to_jslist(BatchStatus.objects.all())}) #since we have a small number of status, this should not be heavy on RAM

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
            fee_prog = fee_prog.objects.get(name__exact=form.cleaned_data['fee_prog'])
            exchange_rate = getattr(currency.objects.get(name__exact=form.cleaned_data['currency']), 'exchange_rate')
            localprice=form.cleaned_data['local_price']
            onlineprice=float(form.cleaned_data['unit_cost'])*exchange_rate
            min_selling = utility.calcultate_min_selling(onlineprice,fee_prog)
            messages.info(request, _("Min selling price is ")+" {0:.2f} ".format(min_selling))
            messages.info(request,_("The diff between Min selling and Local price: ")+" {0:.2f} ".format(min_selling-localprice))
            messages.info(request,_("Profit percent at local price: ")+" {0:.2f} % ".format(utility.calculate_profit_percent(onlineprice,fee_prog,localprice)))
    return render(request, 'calc.html', {'form': calcform})

def getBatchesForProduct(request,product):
    batches=batch.objects.filter(product_type__exact=product,status__in=['FBS','Stock'])
    return render(request,'batchesforproduct.html',{'batches':batches})

def rmsaleorder(request):
    fee_progs=fee_prog.objects.all()
    statuss=BatchStatus.objects.all()
    return render(request,'removesaleorder.html',{'fee_progs':fee_progs,'statuss':statuss})

def changeBatchStatus(request):
    batchObj=batch.objects.get(batch_id__exact=request.META["HTTP_batch_id"])
    utility.edit_statistics(batchObj.status,-batchObj.total_cost)
    batchObj.status=BatchStatus.objects.get(name__exact=request.META["HTTP_NEWVAL"])
    utility.edit_statistics(batchObj.status,batchObj.total_cost)
    batchObj.save()
    return redirect('/rep/batches')

def editCompanyCapital(request):
    utility.new_statistics_value('capital',float(request.META["HTTP_NEWVAL"]))
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