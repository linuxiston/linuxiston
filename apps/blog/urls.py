from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import CategoryViewSet, PostViewSet, CommentViewSet, TagViewSet, VideoPostViewSet, VideoCommentViewSet, \
    UserViewSet
from apps.users.views import user_profile
from .views import (
    home,
    post_detail,
    post_video_detail,
    post_list,
    post_list_category,
    post_list_videos,
    add_like_post,
    add_video_like_post,
    contact,
    write_post,
    about_us,
    liked_posts,
    liked_video_posts,
    user_posts
)

# app_name = "blogs"

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("videoPosts", VideoPostViewSet)
router.register("comments", CommentViewSet)
router.register("videoComments", VideoCommentViewSet)
router.register("tags", TagViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),  # API
    path("maqolalar/", post_list, name="post_list"),
    path("aloqa/", contact, name="contact"),
    path("biz-haqimizda/", about_us, name="about"),
    path("videolar/", post_list_videos, name="post_list_videos"),
    path("maqolalar/yoqtirganlar/", liked_posts, name="liked_posts"),
    path("maqolalar/@<str:username>/", user_posts, name="user_posts"),
    path("maqolalar/yoqtirgan-videolar/", liked_video_posts, name="liked_video_posts"),
    path("maqolalar/<str:category>/", post_list_category, name="post_list_category"),
    path("maqola/<str:slug>/", post_detail, name="post_detail"),
    path("video/<str:slug>/", post_video_detail, name="video_post_detail"),
    path("maqola-yozish/", write_post, name="write-post"),
    path("", home, name="home"),
    # User profile
    path("profile/@<str:username>/", user_profile, name="user-profile"),
]

urlpatterns += [
    path("like/post/<int:pk>/", add_like_post, name="like-post"),
    path("like/videopost/<int:pk>/", add_video_like_post, name="vlike-post"),
]
