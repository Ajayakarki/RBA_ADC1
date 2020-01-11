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

def Register(request):
    return render(request,'shop/Register.html')

def Login(request):
    return render(request,'shop/Login.html')


def customer_registration_form_submission(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return HttpResponse("Welcome" + " " + username)
        else:
            print("Password did not match")

    else:
        return render(request, "shop/Register.html")



def customer_login_form_submission(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponse("<h1> My name is </h1>" + username)

    else:
        return HttpResponse("Could not login" + " " + username)




