from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
        read_only_fields = ('is_admin', 'is_staff', 'email_confirm', 'mobile_confirm')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
