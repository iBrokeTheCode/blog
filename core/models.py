from django.db import models
from django.contrib.auth.models import User

from django_prose_editor.fields import ProseEditorField


# ================================================================
#                               POST
# ================================================================

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = ProseEditorField()
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='posts')  # Default: category.post_set
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts')  # Default: author.post_set
    tags = models.ManyToManyField(
        Tag,
        related_name='posts')  # Default: set.post_set

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created', 'title')

    def __str__(self):
        return self.title

# ================================================================
#                        BUSINESS INFORMATION
# ================================================================


class BusinessInformation(models.Model):
    name = models.CharField(max_length=100)
    about_us = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    # Make unique instance
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Business Information'
        verbose_name_plural = 'Business Information'
        ordering = ('name',)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    identifier = models.CharField(max_length=100, unique=True,
                                  #   choices=[('facebook', 'Facebook'),]
                                  )
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    icon = models.CharField(max_length=100, blank=True)
    business = models.ForeignKey(
        BusinessInformation, on_delete=models.CASCADE, related_name='social_media')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('name',)

    def __str__(self):
        return self.name
