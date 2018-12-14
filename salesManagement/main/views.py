from django.shortcuts import render
from django.shortcuts import redirect
from .forms import productform
# Create your views here.
def addpro(request):
    if request.method=="POST":
        form=productform(commit=False)
        if form.is_valid:
            product=form.save(commit=False)
            product.product_type=request.name
    else:
        form=productform()

    return render(request,'addproduct.html',{'form':form})
def rmit(request):
    return render(request,'removeitem.html')
def addit(request):
    return render(request,'additem.html')
def rep(request):
    return render(request,'reports.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return redirect('accounts/login/')