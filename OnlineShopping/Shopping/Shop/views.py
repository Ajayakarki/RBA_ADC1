from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
	products = Product.objects.all()
	print(products)
	params = {'product': products}
	return render(request, 'shop/index.html',params)

def search(request):
	return HttpResponse("Working on Search")

def contact(request):
	return HttpResponse("Working on Contact")

def viewproduct(request):
	return HttpResponse("Working on View product")

def checkout(request):
	return HttpResponse("Working on CheckOut")

def tryit(request):
	products = Product.objects.all()
	print(products)
	params = {'product': products}
	return render(request, "shop/try.html",params)