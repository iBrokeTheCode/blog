from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created')
    readonly_fields = ('created', 'updated')
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created')
    readonly_fields = ('created', 'updated')
    ordering = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created',
                    'author', 'category', 'post_tags')  # author, tags
    readonly_fields = ('created', 'updated')
    ordering = ('title', '-created', 'author')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    list_filter = ('author', 'category', 'tags')

    def post_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

    post_tags.short_description = 'Tags'  # type: ignore
