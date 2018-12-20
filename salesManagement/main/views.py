from django.shortcuts import render
from django.shortcuts import redirect
from .forms import productform, batchform, salesform
from django.contrib import messages
from .models import commission, batch, currency,sales,product
# Create your views here.


def addpro(request):
    if request.method == "POST":
        form = productform(request.POST,request.FILES)
        if form.is_valid():
            proObj=product()
            proObj.product_type=form.cleaned_data['product_type']
            proObj.name=form.cleaned_data['name']
            proObj.image=request.FILES['image']
            proObj.description=form.cleaned_data['description']
            print(proObj.image)
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
            print(salesObj.product_type)
            salesObj.quant=form.cleaned_data['quant']
            salesObj.saleprice=form.cleaned_data['saleprice']
            salesObj.batchid=form.cleaned_data['batchid']
            salesObj.unitprofit=form.cleaned_data['batchid']
            batchObj = batch.objects.get(batchid__exact=salesObj.batchid)
            batchprice = getattr(batchObj, 'unit_price')
            batchQuant = getattr(batchObj, 'quant')
            if batchQuant > salesObj.quant:
                batch.objects.filter(batchid__exact=salesObj.batchid).update(quant=batchQuant-salesObj.quant)
            elif batchQuant == salesObj.quant:
                batch.objects.filter(batchid__exact=salesObj.batchid).delete()
                salesObj.batchid=None
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
            batchObj.quant=form.cleaned_data['quant']
            batchObj.currency=form.cleaned_data['currency']
            batchObj.unit_price=form.cleaned_data['total_cost']/batchObj.quant
            batchObj.batchid=form.cleaned_data['batchid']
            product_type = getattr(getattr(getattr(batchObj, 'product_type'), 'product_type'), 'product_type')
            exrate = getattr(currency.objects.get(name__exact=batchObj.currency), 'exrate')
            batchObj.unit_price *= exrate
            add = getattr(commission.objects.get(product_type__exact=product_type), 'addfee')
            multiply = getattr(commission.objects.get(product_type__exact=product_type), 'multiplyfee')
            batchObj.minselling = (add+float(batchObj.unit_price))/(1-multiply)
            batchObj.save()
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
