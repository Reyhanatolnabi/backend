from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView

import persons.permissions
from .models import MyUser
from .serializers import MyUserSerializer, AdminSerializer
from .permissions import IsUser


# GET all users
class UsersList(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsAdminUser,)


# GET specific user details
class UserDetail(RetrieveAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (IsUser,)
    serializer_class = AdminSerializer


# create new user only by admin
class CreateUser(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsAdminUser,)


# update specific user details
class UpdateUser(RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (IsUser,)

    def get_serializer_class(self):
        if self.request.user.is_admin:
            self.serializer_class = AdminSerializer
        else:
            self.serializer_class = MyUserSerializer
        return self.serializer_class
