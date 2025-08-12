from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product

# Create your views here.

def say_hello(request):
    # query_set = Product.objects.all()

    # for product in query_set:
    #     print(product)
    
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).first() #none
    # exists = Product.objects.filter(pk=0).exists()
    
    #keyword=value
    # queryset = Product.objects.filter(unit_price__range=(20,300))
    queryset = Product.objects.filter(title__icontains='coffee')


    return render(request , 'hello.html' , { 'name' : 'Sunny' , 'products' : list(queryset)})