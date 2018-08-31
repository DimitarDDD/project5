from django.shortcuts import render, get_object_or_404
from .models import Product 
from .forms import SearchProductForm


# Create your views here.
def all_products(request): 
    products = Product.objects.all()
    
    if "query" in request.GET:
        products = Product.objects.filter(name__contains=request.GET['query'])
        
    if "brand" in request.GET:
        products = Product.objects.filter(brand=request.GET['brand'])
    
    search_form = SearchProductForm(request.GET)
    return render(request, "products.html", {"products": products, 'search_form': search_form})
    
def product_details(request, id):
    product=get_object_or_404(Product, pk=id) 
    return render(request, 'product_details.html',{'product':product })  