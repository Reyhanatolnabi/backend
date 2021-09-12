from django.urls import path
from .views import ProductsList, ProductDetail, CreateProduct, UpdateProduct

app_name = "charity"
urlpatterns = [
    path("list/", ProductsList.as_view(), name="list"),
    path("detail/<int:pk>", ProductDetail.as_view(), name="detail"),
    path("create/", CreateProduct.as_view(), name="create"),
    path("update/<int:pk>", UpdateProduct.as_view(), name="update")
]
