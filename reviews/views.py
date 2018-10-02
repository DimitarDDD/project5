from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm 
from reviews.models import Review
from products.models import Product
from django.contrib import messages
# Create your views here. 


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
        review = form.save()
     
        return redirect(reverse('product_details', args=(product_id,)))
           
 
def edit_a_review(request,pk):  
    review_form = ReviewForm 
    if request.user: 
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

   
  

def delete_review(request):      
    id = request.POST['review_id']      
    pk = request.POST['product_id']      
    product = get_object_or_404(Product, pk=pk)      
    review = get_object_or_404(Review, id=id) 
    if request.method == 'POST':              
            try:
                review.delete()                  
                messages.success(request,'You have successfully deleted the review!')                
            except Review.DoesNotExist:   
                 messages.warning(request, 'The comment review not be deleted.')      
    return redirect('product_details')

        
       
    
      
    
        