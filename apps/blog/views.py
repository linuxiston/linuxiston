from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Tag, Post, VideoPost, Comment, VideoComment, Faq
from apps.users.models import Email
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, EmailForm, CommentVideForm
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


def add_like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.likes.add(request.user)
    return HttpResponse("<h4 class='text-success'> 😍 </h4>")


def add_video_like_post(request, pk):
    post = get_object_or_404(VideoPost, id=pk)
    post.likes.add(request.user)
    return HttpResponse("<h4 class='text-success'> 😍 </h4>")



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
            path = f"{post.get_absolute_url()}#comment-section"
            return HttpResponseRedirect(path)
    else:
        form = CommentForm()
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "single-blog.html", context)


def post_video_detail(request, slug):
    post = get_object_or_404(VideoPost, slug=slug)
    if request.method == "POST":
        form = CommentVideForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            p = VideoComment(
                post=post, author=request.user, comment=comment, created=datetime.now()
            )
            p.save()
            path = f"{post.get_absolute_url()}#comment-section"
            return HttpResponseRedirect(path)
    else:
        form = CommentVideForm()
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "single-video-blog.html", context)
