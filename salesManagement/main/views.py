from django.shortcuts import render

# Create your views here.
def addpro(request):
    return render(request,'addproduct.html')
def rmit(request):
    return render(request,'removeitem.html')
def addit(request):
    return render(request,'additem.html')
def rep(request):
    return render(request,'reports.html')
def home(request):
    return render(request,'home.html')