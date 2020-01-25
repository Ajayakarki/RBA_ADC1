from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from .models import Product, OrderItem, Order
from math import ceil


from .forms import OrderItemForm
# Create your views here.

def index(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	nSlides = n//4 + ceil((n/4)-(n//4))
	cart = 0
	if request.user.username:
		cart = OrderItem.objects.filter(Customer_Id_id = request.user.id).count()
	params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'product': products,"cart":cart}

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


def add_to_cart(request,id):
	#login user object
	user = request.user


	# checking if data is exists or not
	if OrderItem.objects.filter(Customer_Id_id = user.id,item_id = id,ordered = False).exists() :
		#update quantity
		order = OrderItem.objects.filter(Customer_Id_id =user.id,item_id = id).get();
		order.quantity += 1
		order.save()
		messages.info(request, "This item is added to your cart")
		

		# return HttpResponse("updated "+str(order.quantity))
		# if Order.objects.filter(Customer_Id_id = user.id, items_id = id, ordered = False).exists():
		# order = Order.objects.filter(Customer_Id_id =user.id, item_id = id).get();
		# order.quantity +=1
		# order.save()
		# else:

	else:
		#insert a data in a row
		OrderItem.objects.create(item_id = id ,Customer_Id_id = user.id,ordered=False)
		# if not Order.objects.filter(Customer_Id_id = user.id, items_id = id, ordered = False).exists():
		# Order.objects.create(Customer_Id_id =user.id, ordered=False, Ordered_Date = timezone.now())
		#messages.info(request, "This item was already added to your cart")

		#return HttpResponse('created')
	return redirect("My Shop")

def remove_from_cart(request, id):
	user = request.user

	if OrderItem.objects.filter(Customer_Id_id = user.id,item_id = id,ordered = False).exists() :
		order = OrderItem.objects.filter(Customer_Id_id =user.id,item_id = id).get();
		order.quantity= int(order.quantity) - 1
		order.save()
		if int(order.quantity) <= 0:
			order.delete()
		messages.info(request, "This item has been remove from your cart")


	else:
		# OrderItem.objects.create(item_id = id ,Customer_Id_id = user.id,ordered=False)
		messages.info(request, "You donot have any order")
		


	return redirect("My Shop")


def itemdetail(request):
	orderitems = ''
	if request.user.username:
		orderitems = OrderItem.objects.filter(Customer_Id_id = request.user.id).all()

	return render(request,"Shop/item.html",context={"orderitems":orderitems})



def createOrder(request):



	form = OrderItemForm()

	if request.method == 'POST':
		# print('Printing la:', request.POST)
		form = OrderItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')



	context = {'form':form}


	return render(request, 'Shop/orderform.html', context)



# def updateOrder(request, id):
# 	order = OrderItem.objects.get(id=id)
# 	# order = get_object_or_404(OrderItem, id=id)
# 	form = OrderItemForm(instance=order)

# 	if request.method == 'POST':
# 		# print('Printing la:', request.POST)
# 		form = OrderItemForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')



# 	context = {'form':form}


# 	return render(request, 'Shop/orderform.html', context)






	# context = {'form':form}
	# return render(request, 'Shop/orderform.html', context)























































	
	
	# order_item, created = OrderItem.objects.create(
	# 	item=item,
	# 	Customer_Id=request.Customer_Id,
	# 	ordered=False)
	# order_qs = Order.objects.filter(Customer_Id=request.Customer_Id, ordered=False)
	# if order_qs.exists():
	# 	order = order_qs[0]
	# 	#check if the order item is in ythe order
	# 	if order.items.filter(item__id=item.id).exists():
	# 		order_item.quantity +=1
	# 		order_item.save()
	# 	else:
	# 		ordered.items.add(order_item)
	# else:
	# 		ordered_date =timezone.now()
	# 		order = Order.objects.create(Customer_Id=request.Customer_Id, ordered_date=ordered_date)
	# 		order.items.add(order_item)
	# return redirect("Shop:index", id=id )
	# return HttpResponse('hel')
	


