from django.contrib import messages
from django.shortcuts import render,redirect
from .models import FeedBack

# Create your views here.

def Feedback(request):
    return render(request,"Feedback/Feedback.html")

def feedback(request):
    Name= request.POST["Name"]
    Email= request.POST["Email"]
    Subject = request.POST["Subject"]
    Message = request.POST["Message"]


    feedback= FeedBack(Name=Name, Email=Email, Subject=Subject, Message=Message)
    feedback.save()
    messages.info(request, "This item has been remove from your cart")
    return redirect('/')