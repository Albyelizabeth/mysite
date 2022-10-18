

from django.urls import path,include
from .views import index,new_one
urlpatterns = [
    path('',index),
    path('new',new_one,)
] 