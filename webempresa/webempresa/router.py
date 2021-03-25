from rest_framework.routers import DefaultRouter
from blog import api as api_blog

router = DefaultRouter()

router.register('post', api_blog.PostViewSet)
router.register('category', api_blog.CategoryViewSet)
