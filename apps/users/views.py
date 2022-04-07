from django.shortcuts import render
from apps.users.models import User
from django.shortcuts import get_object_or_404


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    print(user.email)
    context = {
        'cuser': user
    }
    return render(request, 'user-profile.html', context)
