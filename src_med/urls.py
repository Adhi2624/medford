from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('products',views.product,name='products'),
    path('carrer',views.carrer,name='carrer'),
    path('aboutus',views.about_us,name='aboutus'),
    path('contact',views.contact,name='contact'),
    
]