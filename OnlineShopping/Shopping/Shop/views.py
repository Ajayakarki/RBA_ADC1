from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	nSlides = n//4 + ceil((n/4)-(n//4))
	params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'product': products}
	return render(request, 'shop/index.html', params)


def search(request):
	return HttpResponse("Working on Search")

def contact(request):
	return HttpResponse("Working on Contact")

def viewproduct(request):
	return HttpResponse("Working on View product")

def checkout(request):
	return HttpResponse("Working on CheckOut")

def about(request):
	return render(request, 'shop/about.html')
