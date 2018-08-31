from django.db import models

# Create your models here.
class Brand(models.Model): 
    name=models.CharField(max_length=100, blank=False, null=False)
    image=models.ImageField(upload_to='images')  
    
    def __str__(self): 
        return self.name
    
