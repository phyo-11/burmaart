from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products":products})
    
def about(request):
    return render(request, "about.html", {})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, "product_detail.html", {'product':product})

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})