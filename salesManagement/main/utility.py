from .models import FeeProgram,Statistics
def calcultate_min_selling(unitCost,fee_prog):
    # Returns the minumin selling price based on the fee prog and the unit cost
    add = getattr(FeeProgram.objects.get(name__exact=fee_prog), 'add_fee')
    multiply = (1-getattr(FeeProgram.objects.get(name__exact=fee_prog), 'multiply_fee')/100) # if the original value saved in DB is 10 multiply would equla 0.9 
    return (add+float(unitCost))/multiply

def calculate_selling_profit_percent(unitCost,fee_prog,percent):
    # Returns the selling price that would result in percent% profit based on fee prog and percent
    add = getattr(FeeProgram.objects.get(name__exact=fee_prog), 'add_fee')
    multiply = 1-(getattr(FeeProgram.objects.get(name__exact=fee_prog), 'multiply_fee')/100)
    return (add+float(unitCost))/(multiply-percent)

def calculate_profit_percent(unitCost,fee_prog,sellingPrice):
    # Returns the profit percent based on the selling price, unit cost and fee prog
    add = getattr(FeeProgram.objects.get(name__exact=fee_prog), 'add_fee')
    multiply = 1-(getattr(FeeProgram.objects.get(name__exact=fee_prog), 'multiply_fee')/100)
    res=((((float(sellingPrice)-add)*multiply)/float(unitCost))-1)*100
    return res

def queryset_to_jslist(queryset):
    # Takes in a quetyset and converys it to a java script list
    res='['
    for q in queryset:
        res=res+'"'+q.name+'"'+','
    res+=']'
    return res

def edit_statistics(name,value):
    # Edits a statistecs field value, either by addition or subtraction, takes in the name
    # and the value to add or sub
    stat,created=Statistics.objects.get_or_create(name__exact=name)
    stat.value+=value
    stat.save()

def new_statistics_value(name,value):
    # Changes the value of a statistics field, takes in the name and the new value
    stat=Statistics.objects.get(name__exact=name)
    stat.value=value
    stat.save()

def create_statistics(name,value):
    # Creates a new statistics field, takes in the value and name
    stat=Statistics()
    stat.name=name
    stat.value=value
    stat.save()