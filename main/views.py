from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products":products})
    
def about(request):
    return render(request, "about.html", {})

def product(request):
    return render(request, "product.html", {})