from django.db import models
from products.models import Product



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.BooleanField(verbose_name="Do you recommend this product? (Click if you recommend)")
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    @property
    def stars(self):
        return range(0,self.rating)
    
    def __str__(self):
        return self.content