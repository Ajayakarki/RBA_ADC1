from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="My Shop"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
    path("viewproduct/", views.viewproduct, name="Show product"),
    path("checkout/", views.checkout, name="CheckOut"),
    path("about/", views.about, name="About RBAClothing"),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('customer_registration_form_submission/', views.customer_registration_form_submission, name='customer_registration_form_submission'),
    path('customer_login_form_submission/', views.customer_login_form_submission, name='customer_login_form_submission')
]
