from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request): 
    return render(request, "cart.html") 
    
def add_to_cart(request, id): 
    quantity=int(request.POST.get('quantity')) 
    
    cart = request.session.get('cart',{}) 
    cart[id] = cart.get(id, quantity) 
    
    request.session['cart'] = cart 
    return redirect('view_cart')
    
def adjust_cart(request,id):  
    quantity = int(request.POST.get('quantity')) 
    cart = request.session.get('cart',{})  
    
    if quantity>0: 
        cart[id] = quantity 
    else: 
        cart.pop[id] 
        
    request.session['cart'] = cart 
    return redirect(reverse('view_cart')) 
    
def delete_item(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')    
    