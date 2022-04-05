from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Tag, Post, VideoPost, Comment, VideoComment, Faq

def home(request):
    left = Post.objects.all()[0]
    right = Post.objects.all()[1]
    video_posts = VideoPost.objects.all()
    faq = Faq.objects.filter(active=True)
    categories = Category.objects.all()
    context = {
        'left': left,
        'right': right,
        'video_posts': video_posts,
        'faq': faq,
        'categories': categories
    }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'single-blog.html', context)


def video_post_detail(request, slug):
    post = get_object_or_404(VideoPost, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog-video.html', context)