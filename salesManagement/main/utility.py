from .models import feeprog,Statistics
def calMinSelling(unitCost,feeProg):
    ''' Returns the minumin selling price based on the fee prog and the unit cost '''
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = (1-getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100) # if the original value saved in DB is 10 multiply would equla 0.9
    return (add+float(unitCost))/multiply

def calSellingatProfitPercent(unitCost,feeProg,percent):
    ''' Returns the selling price that would result in percent% profit based on fee prog and percent '''
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = 1-(getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100)
    return (add+float(unitCost))/(multiply-percent)

def calProfitPercent(unitCost,feeProg,sellingPrice):
    ''' Returns the profit percent based on the selling price, unit cost and fee prog'''
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = 1-(getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100)
    print(unitCost)
    print(feeProg)
    print(sellingPrice)
    print(add)
    print(multiply)
    res=((((float(sellingPrice)-add)*multiply)/float(unitCost))-1)*100
    return res

def querysetToJSlist(queryset):
    res='['
    for q in queryset:
        res=res+'"'+q.name+'"'+','
    res+=']'
    print(res)
    return res

def editStatistics(name,value):
    stat=Statistics.objects.get(name__exact=name)
    stat.value+=value
    stat.save()

def newValueStatistics(name,value):
    stat=Statistics.objects.get(name__exact=name)
    stat.value=value
    stat.save()
def createStatistics(name,value):
    stat=Statistics()
    stat.name=name
    stat.value=value
    stat.save()