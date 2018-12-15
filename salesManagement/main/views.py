from django.shortcuts import render
from django.shortcuts import redirect
from .forms import productform,batchform
from django.contrib import messages
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
    return render(request,'removeitem.html')
def addit(request):
    if request.method=="POST":
        form=batchform(request.POST)
        batch=form.save(commit=False)
        add=commission.objects.only('addfee').get(product_type=batch.product_type)
        batch.minselling=batch.unitprice+
    return render(request,'additem.html')
def rep(request):
    return render(request,'reports.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return redirect('accounts/login/')