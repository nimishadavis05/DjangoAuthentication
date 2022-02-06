from django.urls import path
from accounts.views import *
urlpatterns = [

    path('',Home,name="home"),
    path('register/',register,name="register"),
    path('product',product_view,name="product")
]
