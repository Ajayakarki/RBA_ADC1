from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> My name is Rohit</h1>")

def Register(request):
    return render(request,"Register.html")

def Login(request):
    return render(request,"Login.html")


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
        return render(request, "Register.html")



def customer_login_form_submission(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponse("<h1> My name is </h1>" + username)

    else:
        return HttpResponse("Could not login" + " " + username)




