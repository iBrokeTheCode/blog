from django.contrib import admin

from .models import Category, Post, Tag, BusinessInformation, SocialMedia

# ================================================================
#                               POST
# ================================================================


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

# ================================================================
#                        BUSINESS INFORMATION
# ================================================================


@admin.register(BusinessInformation)
class BusinessInformationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'location', 'user', 'created')
    ordering = ('name', '-created')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('identifier', 'name', 'url', 'business', 'created')
