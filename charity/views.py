from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Products
from .serializers import ProductsSerializer
from persons.permissions import IsUser


class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# GET specific product details
class ProductDetail(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)


# create new user only by admin
class CreateProduct(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)


# update specific user details
class UpdateUser(RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsUser,)

