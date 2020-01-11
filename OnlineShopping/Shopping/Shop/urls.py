from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="My Shop"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
    path("viewproduct/", views.viewproduct, name="Show product"),
    path("checkout/", views.checkout, name="CheckOut"),
    path("about/", views.about, name="About RBAClothing"),
    path("UserSession/", views.UserSession, name="UserSession"),
]
