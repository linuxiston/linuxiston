from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import CategoryViewSet, PostViewSet, CommentViewSet, TagViewSet
from .views import home, post_detail, video_post_detail, post_list

# app_name = "blogs"

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("tags", TagViewSet)


urlpatterns = [
    path("api/", include(router.urls)), # API
    path('maqolalar/', post_list, name='post_list'),
    path('maqola/<str:slug>/', post_detail, name='post_detail'),
    path('video/<str:slug>/', video_post_detail, name='video_post_detail'),
    path('', home, name='home'),
]
