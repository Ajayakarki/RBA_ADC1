from django.urls import path
from .import views 

urlpatterns = [
    path("", views.index, name="My Shop"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
    path("viewproduct/", views.viewproduct, name="Show product"),
    path("checkout/", views.checkout, name="CheckOut"),
    path("about/", views.about, name="About RBAClothing"),
    path("add-to-cart/<int:id>", views.add_to_cart, name="addtocart"),
    path("remove-from-cart/<int:id>", views.remove_from_cart, name="removefromcart"),
    path("itemdetail/",views.itemdetail,name="itemdetail"),
    path("create-order/",views.createOrder,name="createOrder"),
    # path("update-order/<int:id>",views.updateOrder,name="updateOrder"),



]
