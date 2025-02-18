


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages

 

# Create your views here.


def shp_login(req):
    if 'watch' in req.session:
        return redirect(shp_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['watch']=uname   #create session
                return redirect(shp_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(shp_login)
    
    else:
        return render(req,'login.html')
    

def shp_login1(req):
    if 'watch' in req.session:
        return redirect(shp_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['watch']=uname   #create session
                return redirect(shp_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(shp_login)
    
    else:
        return render(req,'login.html')

def shp_home(req):
    if 'watch' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'data':data})
    else:
        return redirect(shp_login)

def shp_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(shp_login)








def add_prod(req):
    if 'watch' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            img=req.FILES['img']
            prd_dis=req.POST['prd_dis']
            quantity = int(req.POST['quantity'])  # Fetch quantity from form
            data=Product.objects.create(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,img=img,dis=prd_dis,quantity=quantity)
            data.save()
            return redirect(add_prod)
        else:
            return render(req,'shop/add_pro.html')
    else:
        return redirect(shp_login)
    
def edit_prod(req,pid):
    if 'watch' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            prd_dis=req.POST['prd_dis']
            img=req.FILES.get('img')
            quantity = req.POST['quantity']  # Retrieve quantity
            if img:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,dis=prd_dis,quantity=quantity)
                data=Product.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,dis=prd_dis,quantity=quantity)
            return redirect(shp_home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit.html',{'product':data})
    else:
        return redirect(shp_login)
def delete_prod(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('static/'+og_path)
    data.delete()
    return redirect(shp_home)





def booking(request):
    # Get all Buy objects with related product and user data
    buy = Buy.objects.select_related('product', 'user').all().order_by('-date')
    
    # Get all Order objects related to the Buy objects (assuming there's a way to link Buy to Order)
    orders = Order.objects.all()

    # Create combined data
    combined_data = zip(buy, orders)

    return render(request, 'shop/booking.html', {'combined_data': combined_data})




def delete_booking(request, order_id):
    # Fetch the booking (order) object
    order = get_object_or_404(Order, id=order_id)  # Assuming `Order` is your model
    order.delete()  # Delete the order from the database

    # Redirect back to the bookings page after deletion
    return redirect(booking)  # Replace 'bookings' with the name of your bookings view URL





from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string

# Mock function to simulate email sending for verification
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'



#------------------------user--------------------------------

def profile(req):
    data = Product.objects.all()  # Get all products from the database
    return render(req, 'profile.html', {'data': data, 'user': req.user})


def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        # send_mail('user registration','watch account created', settings.EMAIL_HOST_USER, [email])
        try:
           
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shp_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/register.html')

def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'data':data})
    else:
        return redirect(shp_login)
    
def view_pro(req,pid):
        data=Product.objects.get(pk=pid)
        return render(req,'user/view_pro.html',{'data':data})



def add_to_cart(req,pid):
    prod=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.create(user=user,product=prod)
    data.save()
    return redirect(view_cart)




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, User, Buy, Cart

def user_buy(req, cid):
    user = User.objects.get(username=req.session['user'])
    cart = Cart.objects.get(pk=cid)
    product = cart.product
    quantity = cart.quantity  # Get the quantity from the cart
    
    # Create a Buy object (purchase)
    buy = Buy.objects.create(user=user, product=product, price=product.ofr_price, quantity=quantity)
    buy.save()
    
    # Reduce the product stock based on the quantity purchased
    product.quantity -= quantity
    product.save()

    # Remove the product from the cart after purchase
    cart.delete()

    # Redirect to order or confirmation page
    return redirect('order')  # Or whatever view shows the order summary





def user_booking(req):
    user = User.objects.get(username=req.session['user'])
    bookings = Buy.objects.filter(user=user)

    # Add total price for each booking item
    for booking in bookings:
        booking.total_price = booking.price * booking.quantity

    return render(req, 'user/user_booking.html', {'buy': bookings})








def user_buy1(req, pid):
    user = User.objects.get(username=req.session['user'])
    product = Product.objects.get(pk=pid)
    
    # Check if the product is out of stock (quantity is zero)
    if product.quantity == 0:
        # If the product is out of stock, show an alert message
        messages.error(req, 'Sorry, this product is currently out of stock and cannot be purchased.')
        return redirect('view_product', pid=pid)  # Redirect back to the product page with the alert
    
    # Continue with the purchase process if the product is in stock
    price = product.ofr_price
    buy = Buy.objects.create(user=user, product=product, price=price)
    buy.save()
    
    # Reduce the stock quantity of the product
    product.quantity -= 1
    product.save()

    # Redirect to the order confirmation or view
    return redirect('order')




    






from django.shortcuts import render, redirect
from .form import OrderForm
from .models import Order

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Redirect to success page
    else:
        form = OrderForm()
    
    return render(request, 'user/product_booking.html', {'form': form})

def order_success(request):
    return render(request, 'user/order.html')








from django.shortcuts import render, redirect
from .models import Cart, Product

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_cart_price = sum(item.total_price for item in cart_items)

    # Check if any product in the cart is out of stock
    for item in cart_items:
        item.is_out_of_stock = item.product.quantity == 0

    return render(request, 'user/view_cart.html', {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price
    })

def update_cart_quantity(request, id, quantity):
    try:
        cart_item = Cart.objects.get(id=id, user=request.user)
        product = cart_item.product

        # Update quantity if it's valid and within the available stock
        if 0 < quantity <= product.quantity:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect('view_cart')
    except Cart.DoesNotExist:
        return redirect('view_cart')

def delete_cart(request, id):
    try:
        Cart.objects.get(id=id, user=request.user).delete()
    except Cart.DoesNotExist:
        pass
    return redirect('view_cart')
















from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Buy  # Import your Buy model

def cancel_buy(request, buy_id):
    buy = get_object_or_404(Buy, pk=buy_id)
    
    # Perform cancellation logic (e.g., delete or update status)
    buy.delete()  # Or buy.status = "Cancelled" and buy.save()
    
    messages.success(request, "Your purchase has been canceled successfully.")
    return redirect(user_booking)  # Redirect to the buy list page
















