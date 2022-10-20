from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Product

# Create your views here.-


def index(request):
    d = {
        "name": "Arun",
        "age" : 30,
        
    }
    
    li = ["Allen","Alwin","Sreerag","Allu"]
    
    for i in range(0,10):
      print(i)
      
    context = {'li':li}
    
    
    return render(request, 'myapp/index.html',context=context)


def new_one(request):
    return render(request, 'listing/new_one.html')

def products(request):
    p = Product.objects.all()
    
    context = {'products':p}
    
    return render(request, 'myapp/products.html',context=context)


def product_details(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    return render(request, 'myapp/product_details.html',context=context)


def add_product(request):
    p = Product(name = "Samsung 32 Inch Monitor",price = 36000.0)
    
    p.description = "This is a Samsung 32 Inch Monitor"

    p.save()
    
    return HttpResponse(p)
