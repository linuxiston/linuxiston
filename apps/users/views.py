from django.shortcuts import render
from apps.users.models import User
from django.shortcuts import get_object_or_404
from apps.blog.models import Post, VideoPost
from .forms import UserForm
from django.contrib import messages


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts_count = Post.objects.filter(author=user).count()
    likes_count = Post.objects.filter(likes__username=user.username).count() + VideoPost.objects.filter(
        likes__username=user.username).count()
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            obj = user_form.save(commit=False)
            obj.save()
            messages.success(request, "Ma'lumotlarizngiz yangilandi")
        else:
            messages.warning(request, "Ma'lumotlaringizni to'liq kiriting")
    context = {
        'cuser': user,
        'posts_count': posts_count,
        'likes_count': likes_count
    }
    if user == request.user:
        return render(request, 'user-profile.html', context)
    return render(request, 'other-user-profile.html', context)
