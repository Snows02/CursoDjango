"""Posts admin."""

# Django
from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'user',
        'title',
        'photo',
    )
    search_fields = (
        'user',
        'title',
    )
