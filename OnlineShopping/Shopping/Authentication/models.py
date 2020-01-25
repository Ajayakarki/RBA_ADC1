from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	Customer_Id = models.CharField(max_length=10)
	Customer_Name = models.CharField(max_length=250)
	Customer_Address = models.CharField(max_length=50)
	Customer_Contact = models.CharField(max_length=10)
	Customer_Password = models.CharField(max_length=50)
	Customer_Email = models.EmailField()

