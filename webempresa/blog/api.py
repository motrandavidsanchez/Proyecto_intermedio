from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from blog.models import Post, Category
from blog.serializers import PostSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
