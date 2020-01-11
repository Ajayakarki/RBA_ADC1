from django.db import models

# Create your models here.

class Product(models.Model):
	Product_Id = models.AutoField
	Product_Name = models.CharField(max_length=100)
	Product_Price = models.IntegerField(default=0)
	Product_Description = models.TextField()
	Publication_Date = models.DateField()
	Product_Category = models.CharField(max_length=100, default="")
	Product_Image = models.ImageField(upload_to='shop/images', default="")


	def __str__(self):
		return self.Product_Name

