from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def account(request):
    return HttpResponse("test views")
