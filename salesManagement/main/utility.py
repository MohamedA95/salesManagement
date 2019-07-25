from .models import feeprog
def calMinSelling(unitprice,feeProg):
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100
    return (add+float(unitprice))/(1-multiply)

def calProfitPercent(unitprice,feeProg,percent):
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100
    return (add+float(unitprice))/(1-multiply-percent)