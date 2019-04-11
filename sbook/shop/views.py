from django.shortcuts import render
from .models import Product, Contact, Orders
from math import ceil
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse

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

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address= request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        year=request.POST.get('year','')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email,room_no=address,year=year,phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
def product(request):
    if request.method=="POST" and request.FILES['imag']:
        image=request.FILES['imag']
        fs=FileSystemStorage()
        fs.save(image.name,image)
        image=image
        name=request.POST.get('name','')
        category=request.POST.get('category','')
        price=request.POST.get('price','')
        desc=request.POST.get('desc','')
        phone=request.POST.get('phone','')
        product=Product(product_name=name,category=category,price=price,desc=desc,image=image,phone=phone)

        product.save()
        sel=True

        #chk=True

    return render(request,'shop/product.html')

