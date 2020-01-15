"""Post forms."""

# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
