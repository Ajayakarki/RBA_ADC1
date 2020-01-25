from django.shortcuts import render,redirect
from .models import Invoice


def Checkout(request):
    return render(request,"Payment/Checkout.html")

def invoice(request):
    ship= request.POST["ship"]
    contact= request.POST["contact"]
    amount = request.POST["amount"]
    id = request.POST["id"]


    invoice= Invoice(shipping_address=ship, Amount=amount, Contact=contact, Customer_Id_id=id)
    invoice.Customer_Id= request.user
    invoice.save()
    return redirect('/')

