

from django.urls import path,include
from .views import index,new_one,products,product_details,add_product
urlpatterns = [
    path('',index),
    path('new/',new_one),
    path('products/',products,name='products'),
    path('products/<int:id>',product_details,name='product_details'),
    path('product/add',add_product,name='add_product'),
] 