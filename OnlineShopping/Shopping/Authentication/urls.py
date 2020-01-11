from django.urls import path
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('customer_registration_form_submission/', views.customer_registration_form_submission, name='customer_registration_form_submission'),
    path('customer_login_form_submission/', views.customer_login_form_submission, name='customer_login_form_submission')
]