from rest_framework import viewsets
from .models import Category, Post, VideoPost, Comment, VideoComment, Tag, User

from .serializers import (
    CategorySerializer,
    PostSerializer,
    VideoPostSerializer,
    CommentSerializer,
    VideCommentSerializer,
    TagSerializer,
    UserSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VideoPostViewSet(viewsets.ModelViewSet):
    queryset = VideoPost.objects.all()
    serializer_class = VideoPostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class VideoCommentViewSet(viewsets.ModelViewSet):
    queryset = VideoComment.objects.all()
    serializer_class = VideCommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
