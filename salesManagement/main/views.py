from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from .forms import productform, batchform, salesform,calcform
from .models import  batch, currency,sales,product,feeprog
from .serializer import productSerliz,batchSerliz,salesSerliz,feeprogSerliz
from . import utility
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
            messages.info(request, "Product added successfully!")
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
                messages.error(request, "The product is not in this batch, please choose the correct batch!")
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
                messages.error(request, "Either the product is not added or the Quantity is larger than the avalible!")
                return render(request, 'removeitem.html', {'form': salesform})
            salesObj.unitprofit = salesObj.saleprice-batchprice
            salesObj.totalprofit = salesObj.unitprofit*salesObj.quant
            salesObj.profitpercent = (salesObj.unitprofit/salesObj.saleprice)*100
            salesObj.save()
            messages.info(request, "Item removed successfully!")
        else:
            for e in form.errors:
                messages.error(request, "ERROR:"+e)
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
            batchObj.batchid=form.cleaned_data['batchid']
            exrate = getattr(currency.objects.get(name__exact=batchObj.currency), 'exrate')
            batchObj.unit_price *= exrate
            batchObj.total_cost=form.cleaned_data['total_cost']*exrate
            batchObj.minselling = utility.calMinSelling(batchObj.unit_price,batchObj.feeprog)
            batchObj.profit10 = utility.calProfitPercent(batchObj.unit_price,batchObj.feeprog,0.1)
            batchObj.save()
            product.objects.filter(name__exact=form.cleaned_data['product_type']).update(avalible=True)
            messages.info(request, "Item added successfully!")
        else:
            for e in form.errors:
                messages.error(request, "ERROR:"+e)
    return render(request, 'additem.html', {'form': batchform})

def repsales(request):
    return render(request, 'repsales.html')

def repproducts(request):
    return render(request, 'repproducts.html')

def repbatches(request):
    return render(request, 'repbatches.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return redirect('/accounts/login/')

def calc(request):
    if request.method=="POST":
        form=calcform(request.POST)
        if form.is_valid() :
            fee_prog = feeprog.objects.get(name__exact=form.cleaned_data['feeprog'])
            add = getattr(fee_prog, 'addfee')
            multiply = getattr(fee_prog, 'mulfee')/100
            exrate = getattr(currency.objects.get(name__exact=form.cleaned_data['currency']), 'exrate')
            localprice=form.cleaned_data['local_price']
            onlineprice=float(form.cleaned_data['unit_cost'])*exrate
            minselling = add+onlineprice/(1-multiply)
            messages.info(request, "Min selling price is "+str(minselling)+" The diff between Min selling and Local price is "+str(localprice-minselling))
    return render(request, 'calc.html', {'form': calcform})

def getBatchesForProduct(request,product):
    print("product")
    print(product)    
    batches=batch.objects.filter(product_type__exact=product)
    print("product")
    print(product)
    print("batches")
    print(batches)
    return render(request,'batchesforproduct.html',{'batches':batches})