from django.urls import path
from .views import UsersList, UserDetail, CreateUser, UpdateUser

app_name = "persons"

urlpatterns = [
    path("list/", UsersList.as_view(), name="list"),
    path("detail/<int:pk>", UserDetail.as_view(), name="detail"),
    path("create/", CreateUser.as_view(), name="create"),
    path("update/<int:pk>", UpdateUser.as_view(), name="update")

]
