from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Tag, Post, VideoPost, Comment, VideoComment, Faq
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def post_list(request):
    query = request.GET.get('qidirish')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        posts = Post.objects.all()
    page_num = request.GET.get('sahifa', 1)
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)


def post_list_category(request, category):
    category = get_object_or_404(Category, category=category)
    posts = Post.objects.filter(category=category)
    page_num = request.GET.get('sahifa', 1)
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog-category.html', context)


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