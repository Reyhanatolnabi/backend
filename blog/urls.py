from django.urls import path
from .views import ArticleListAPI, ArticleDetails

app_name = "blog"
urlpatterns = [
    path('articles/', ArticleListAPI.as_view()),
    path('articles/<int:pk>/', ArticleDetails.as_view()),
]
