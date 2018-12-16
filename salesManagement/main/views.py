from django.shortcuts import render
from django.shortcuts import redirect
from .forms import productform,batchform,salesform
from django.contrib import messages
from .models import commission,batch
# Create your views here.
def addpro(request):
    if request.method=="POST":
        form=productform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Product added successfully!")
        else:
            messages.error(request,"A product with that name already exists!")
    return render(request,'addproduct.html',{'form':productform})
def rmit(request):
    if request.method=="POST":
        form=salesform(request.POST)
        if form.is_valid():
            sales=form.save(commit=False)
            salesBatchid=getattr(getattr(sales,'batchid'),'uid')
            batchObj=batch.objects.get(uid__exact=salesBatchid)
            buyprice=getattr(batch.objects.get(uid__exact=salesBatchid),'unit_price')
            currentQuant=getattr(batchObj,'quant')
            if currentQuant<=sales.quant:
                batch.objects.filter(uid__exact=salesBatchid).update(quant=currentQuant-sales.quant)
            sales.unitprofit=sales.saleprice-buyprice
            sales.totalprofit=(sales.saleprice-buyprice)*sales.quant
            sales.save()
            form.save_m2m()
            messages.info(request,"Item removed successfully!")
        
    return render(request,'removeitem.html',{'form':salesform})
def addit(request):
    if request.method=="POST":
        form=batchform(request.POST)
        if form.is_valid():
            batch=form.save(commit=False)
            product_type=getattr(getattr(getattr(batch,'product_type'),'product_type'),'product_type')
            add=getattr(commission.objects.get(product_type__exact=product_type),'addfee')
            multiply=getattr(commission.objects.get(product_type__exact=product_type),'multiplyfee')
            batch.minselling=(add+float(batch.unit_price))/(1-multiply)
            batch.save()
            form.save_m2m()
            messages.info(request,"Item added successfully!")
        else:
            for e in form.errors:
                messages.error(request,"ERROR:"+e)
    return render(request,'additem.html',{'form':batchform})

def repsales(request):
    return render(request,'reports.html')

def repproducts(request):
    return render(request,'reports.html')

def repbatches(request):
    return render(request,'reports.html')

def home(request):
    return render(request,'home.html')
def login(request):
    return redirect('accounts/login/')