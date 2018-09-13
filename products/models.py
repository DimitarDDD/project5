from django.db import models
from brands.models import Brand

# Create your models here.
class Product(models.Model): 
    name=models.CharField(max_length=100, blank=False, null=False)
    description =models.TextField(default="Enter Descriptio")
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='images')  
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    
    def average_rating(self): 
        if self.reviews_received.all():
            average = self.reviews_received.all().aggregate(Avg('rating'))
            n = average['rating__avg']
            return float(round(n, 2))
        else:
            return 0
        


    
    def __str__(self): 
        return self.name
     
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField()