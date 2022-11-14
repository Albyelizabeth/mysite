from django.shortcuts import render
from myapp.models import Product
# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import AddProductSerializer,UserSerializer,ProductSerializer


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class =ProductSerializer


 


