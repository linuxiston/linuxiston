from django.contrib import admin
from .models import Category, Tag, Post, Comment

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'category', 'number_of_likes')
    list_filter = ('category', 'created')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
