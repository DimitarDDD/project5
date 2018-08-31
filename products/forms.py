from django import forms
from .models import Product

class SearchProductForm(forms.ModelForm):
    
    query = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = Product
        fields = ['query','brand']