from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from products.models import Product

# Create your views here. 
def review_content(request,pk):
    product = get_object_or_404(Product)
    review = get_object_or_404(Review, pk=pk)
    review.save()
    return render(request, "review_content.html", {'review': review}) 

def add_a_review(request,pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    product_id = int(request.POST['product'])
    product = get_object_or_404(Product, pk=product_id)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author= request.user
        review.product = product
        review.save()
        return redirect(reverse('product_details' args=(product_id)))
           
 
def edit_a_review(request,pk):  
     if request.user:
        product = get_object_or_404(Product)
        review = get_object_or_404(Review, pk=pk)if pk else None
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review_form.save()
                return redirect('products')
        else: 
            review_form = ReviewForm(instance=review)
        return render(request, "edit_a_review.html", {'review_form': review_form})  

   
  
def delete_review(request, pk=None):

    if request.user:
        product = get_object_or_404(Product)
        review = get_object_or_404(Review, pk=pk) if pk else None
        review.delete()

    else: 
        return redirect(reverse('product_details'))
        
       
    
      
    
        