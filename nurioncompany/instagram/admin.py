from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ["created_at", "is_public"]
    search_fields = ["message"]

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" width="100" height="100"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass