from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Tag, Post, VideoPost, Comment, VideoComment, Faq
from apps.users.models import Email
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, EmailForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    left = Post.objects.all()[0]
    right = Post.objects.all()[1]
    video_posts = VideoPost.objects.all()
    faq = Faq.objects.filter(active=True)
    categories = Category.objects.all()
    if request.method == "POST":
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            email = emailform.cleaned_data["email"]
            path = f"{request.META.get('HTTP_REFERER')}"
            if Email.objects.filter(email=email).exists():
                messages.info(request, "Hmm. Siz allaqachon a'zo bo'lgansiz 😊")
            else:
                p = Email(email=email, created=datetime.now())
                p.save()
                messages.success(
                    request,
                    "Ajoyib! Email xabarnomaga muvaffaqiyatli a'zo bo'ldingiz 🤗",
                )
            return HttpResponseRedirect(path)
    else:
        emailform = EmailForm()
    context = {
        "left": left,
        "right": right,
        "video_posts": video_posts,
        "faq": faq,
        "categories": categories,
    }
    return render(request, "index.html", context)


def post_list(request):
    query = request.GET.get("qidirish")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        posts = Post.objects.all()
    page_num = request.GET.get("sahifa", 1)
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)


def post_list_category(request, category):
    category = get_object_or_404(Category, category=category)
    posts = Post.objects.filter(category=category)
    page_num = request.GET.get("sahifa", 1)
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts, "category": category}
    return render(request, "blog-category.html", context)


def post_list_videos(request):
    posts = VideoPost.objects.all()
    page_num = request.GET.get("sahifa", 1)
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts,
    }
    return render(request, "blog-video.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            p = Comment(
                post=post, author=request.user, comment=comment, created=datetime.now()
            )
            p.save()
    else:
        form = CommentForm()
    related_posts = Post.objects.filter(category=post.category)
    left = Post.objects.all()[0]
    right = Post.objects.all()[1]
    context = {
        "post": post,
        "form": form,
        "related_posts": related_posts,
        "left": left,
        "right": right,
    }
    return render(request, "single-blog.html", context)


def video_post_detail(request, slug):
    post = get_object_or_404(VideoPost, slug=slug)
    context = {"post": post}
    return render(request, "blog-video.html", context)
