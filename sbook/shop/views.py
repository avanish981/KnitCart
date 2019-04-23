from django.shortcuts import render
from .models import Product, Contact, Orders
from django.shortcuts import redirect
from math import ceil
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from shop.forms import UserCreateForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from shop.models import Signup
from django.contrib.auth.models import User
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse


'''print("hello world")
with connection.cursor() as cursor:

        try:
         print("try")

         cursor.execute("SELECT * FROM Product")
         for row in cursor:
             print(row)

        except:

            print("not execute")

            pass'''
registered=0
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name,email=email,phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'shop/prodView.html', {'product':product[0]})
@login_required
def checkout(request):

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address= request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        year=request.POST.get('year','')
        phone = request.POST.get('phone', '')
        product_name=request.POST.get('product','')
        order = Orders(items_json=items_json, name=name, email=email,room_no=address,year=year,phone=phone,product_name=product_name)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
@login_required
def product(request):

    if request.method=="POST" and request.FILES['imag']:
        user=User.objects.get(username=request.user.username)
        image=request.FILES['imag']
        fs=FileSystemStorage()
        fs.save(image.name,image)
        image=image
        name=request.POST.get('name','')
        category=request.POST.get('category','')
        price=request.POST.get('price','')
        desc=request.POST.get('desc','')
        #phone=request.POST.get('phone','')
        price1=request.POST.get('price1','')
        product=Product(product_name=name,category=category,price=price,desc=desc,image=image,user=user)
        product.save()
        sel=True
        con={"sel":sel}
        #chk=True
        return render(request,'shop/product.html',con)

    return render(request,'shop/product.html')
def signup(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print('helo')
            return redirect('/login')
            print('2')
        else:
            form = UserCreateForm()
            messages.error(request, "Password doesnot match or username already exist")
            return render(request, 'shop/signup.html', {'form': form})
    return render(request, 'shop/signup.html', {'form': form})

def log_in(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Incorrect Username or Password")
            return render(request,'shop/login.html')
    else:
        return render(request,'shop/login.html')
def log_out(request):
    #Euser=UserCreationForm(request)
    logout(request)
    return redirect('/')
def account(request):
    user=User.objects.get(username=request.user.username)
    product=Product.objects.filter(user=user)
    for i in product:
        print(i)
    con={"product":"product"}
    return render(request,'shop/account.html',{'product':product})
