from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="author-avatars")
    bio = models.CharField(max_length=300)
    telegram = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.full_name


class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=20)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="post-thumbnails")
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    slug = models.SlugField()
    active = models.BooleanField(default=True)

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])  # not created yet

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created",)
        verbose_name = "post"
        verbose_name_plural = "Blog posts"


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Post)


class VideoPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    description = models.CharField(max_length=300)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="post-thumbnails")
    likes = models.ManyToManyField(User, blank=True, related_name="vlikes")
    slug = models.SlugField()

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("video_post_detail", args=[str(self.slug)])  # not created yet

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created",)
        verbose_name = "Video post"
        verbose_name_plural = "Video blog posts"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) + " + " + str(self.created) + str(self.author)

    class Meta:
        ordering = ("-created",)
        verbose_name = "comment"
        verbose_name_plural = "Comments"


class VideoComment(models.Model):
    post = models.ForeignKey(
        VideoPost, related_name="video_comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) + " + " + str(self.created) + str(self.author)

    class Meta:
        ordering = ("-created",)
        verbose_name = "video comment"
        verbose_name_plural = "Video Comments"


# QA section
class Faq(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Faq"
        verbose_name_plural = "FAQ"
        ordering = ("-created",)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    answered = models.BooleanField(default=False)
    sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-sent",)
        verbose_name = "contact"
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.email
