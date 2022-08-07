from django.contrib import admin

from .models import News, Comment

admin.site.register(News)


class CommentAdmin(admin.ModelAdmin):
    """Админка."""
    list_display = ('pk', 'post', 'author', 'text', 'created')
    list_filter = ('author',)
    search_fields = ('author', 'created')


admin.site.register(Comment, CommentAdmin)
