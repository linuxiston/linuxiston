from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, PostViewSet, CommentViewSet, TagViewSet

app_name = "blogs"

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("tags", TagViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
