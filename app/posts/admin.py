from django.contrib import admin

from .models import Post, PostLike


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'timestamp',
        'likes_count',
    ]
    ordering = [
        'user',
        'title',
        'timestamp',
        'likes_count',
    ]
    search_fields = [
        'title',
        'description',
        'content',
    ]
    list_filter = [
        'timestamp',
    ]
    list_per_page = 50


class PostLikeAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'user',
        'timestamp',
    ]
    ordering = [
        'post',
        'user',
        'timestamp',
    ]
    search_fields = [
        'post',
        'user',
    ]
    list_filter = [
        'timestamp',
    ]
    list_per_page = 50


admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
