from rest_framework import permissions
from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly


class ArticleListAPI(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ArticleDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
