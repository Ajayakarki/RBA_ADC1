from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth


from .models import Product
# Create your views here.

def index(request):
	return render(request, 'shop/index.html')


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

def UserSession(request):
	return render(request, 'shop/UserSession.html')



