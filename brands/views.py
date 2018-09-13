from django.shortcuts import render
from .models import Brand


# Create your views here.
def all_brands(request): 
    brands= Brand.objects.all()
    return render(request, "brands.html", {"brands": brands})