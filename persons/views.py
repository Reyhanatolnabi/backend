from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import MyUser
from .serializers import MyUserSerializer
from .permissions import IsUser


# GET all users
class UsersList(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsAdminUser,)


# GET specific user details
class UserDetail(RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsUser,)


# create new user only by admin
class CreateUser(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsAdminUser,)


# update specific user details
class UpdateUser(RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsUser,)


