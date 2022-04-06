from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import CategoryViewSet, PostViewSet, CommentViewSet, TagViewSet
from .views import (
    home,
    post_detail,
    post_video_detail,
    post_list,
    post_list_category,
    post_list_videos,
    add_like_post,
    add_video_like_post
)

# app_name = "blogs"

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("api/", include(router.urls)),  # API
    path("maqolalar/", post_list, name="post_list"),
    path("videolar/", post_list_videos, name="post_list_videos"),
    path("maqolalar/<str:category>/", post_list_category, name="post_list_category"),
    path("maqola/<str:slug>/", post_detail, name="post_detail"),
    path("video/<str:slug>/", post_video_detail, name="video_post_detail"),
    path("", home, name="home"),
]

urlpatterns += [
    path('like/post/<int:pk>/', add_like_post, name='like-post'),
    path('like/videopost/<int:pk>/', add_video_like_post, name='vlike-post'),
]
