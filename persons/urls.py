from django.urls import path
from . import views

app_name = "persons"
urlpatterns = [
    path("", views.register, name="register"),
    path("", views.login, name="login"),
]
