from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q , F
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
    # queryset = Product.objects.filter(title__icontains='coffee')

    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)


    # Products: inventory <10 OR price <20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    queryset = Product.objects.filter(inventory=F('collection__id'))

    


    return render(request , 'hello.html' , { 'name' : 'Sunny' , 'products' : list(queryset)})