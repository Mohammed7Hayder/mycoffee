from django.shortcuts import get_object_or_404 , render
from datetime import datetime
from .models import Product


# Create your views here.

def products(request):
    #pro = Product.objects.all(),
    
  #  name = None
    
  #  desc = None
  ##     if name:
   #     pro = pro.filter(name__icontains='name')
  #    
  #  if 'searchdesc' in request.GET:
    #    desc = request.GET['searchdesc']
    #    if desc:
     #      pro = pro.filter(desc__icontains=name)  
     # 

    context = {
        
        'products': Product.objects.all(),
    }
     
    return render(request , 'products/products.html', context)

def product(request , pro_id):
    
    contex = {
        'pro':get_object_or_404(Product, pk = pro_id)
    }
    return render(request, 'products/porduct.html',contex)

def searsh(request):
    return render(request, 'products/search.html')




def vie_sea(request):
    pro = Product.objects.all()
    
    
    name= None
    desc= None
    pfrom = None
    pto = None
    if 'searchname' in request.GET:
        name= request.GET['searchname']
        if name:
            pro = pro.filter(name__icontains=name)
            
    if 'searchdesc' in request.GET:
        desc= request.GET['searchdesc']
        if desc:
            pro = pro.filter(descripton__icontains=desc)
            
    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        
        pfrom = request.GET['searchpricefrom']
        pto = request.GET['searchpriceto']
        if pfrom and  pto:
            if pfrom.isdigit() and pto.isdigit():
                pro = pro.filter( price__gte=pfrom , price__lte=pto )

        
        
    
        
        
    context = {
        
        'products': pro
        
    }
    
    return render(request, 'products/vie_sea.html',context )


#Feed.objects.filter(location__areaHash__istartwith='*****')
#Feed.objects.filter(location__areaHash__istartswith='*****')