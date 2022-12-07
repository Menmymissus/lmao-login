from django.contrib import admin
from django.urls import path
from qhome import views

urlpatterns = [
    path("",views.index),
    path("home",views.home),
    path("contact",views.contact),
    path("#",views.home),
    path("#",views.contact),


    
]