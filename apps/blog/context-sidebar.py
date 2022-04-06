from .models import Category, Post, VideoPost


def sidebar(request):
    return {
        "sidebar_cats": Category.objects.all(),
        "sidebar_posts": Post.objects.all()[:4],
        "sidebar_video_posts": VideoPost.objects.all()[:4],
    }
