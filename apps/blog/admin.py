from django.contrib import admin
from .models import Category, Tag, Post, VideoPost, Comment, VideoComment, Faq, Contact
from apps.users.models import Email

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(VideoComment)
admin.site.register(Faq)
admin.site.register(Email)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "category", "number_of_likes", "active")
    list_filter = ("category", "created", "active")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(VideoPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "video_url", "created", "category", "number_of_likes")
    list_filter = ("category", "created")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'answered', 'sent')
    list_filter = ('answered', 'sent')
    search_fields = ('name', 'email')
