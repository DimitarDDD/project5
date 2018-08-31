from django.db import models
from brands.models import Brand

# Create your models here.
class Product(models.Model): 
    name=models.CharField(max_length=100, blank=False, null=False)
    description =models.TextField(default="Enter Descriptio")
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='images')  
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    
    
    def __str__(self): 
        return self.name
    