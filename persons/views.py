from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("This is a simple register")


def login(request):
    return HttpResponse("This is a simple login")
