from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Products, Category
from mptt.admin import MPTTModelAdmin

admin.site.register(Products)
admin.site.register(Category, MPTTModelAdmin)
