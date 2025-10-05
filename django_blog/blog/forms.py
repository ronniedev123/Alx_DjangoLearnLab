# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput
from .models import Profile
from .models import Post
from .models import Comment
from .models import Tag

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Comma-separated list of tags (e.g. django,python,web).'
    )

    class Meta:
        model = Profile
        fields = ["title", "body", "tags", "bio", "avatar"]

        def __init__(self, *args, **kwargs):
        # If we pass instance, populate tags field from instance.tags
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            tag_names = ', '.join([t.name for t in self.instance.tags.all()])
            self.fields['tags'].initial = tag_names

    def clean_tags(self):
        tags_text = self.cleaned_data.get('tags', '')
        # remove double spaces and empty parts
        tag_names = [t.strip() for t in tags_text.split(',') if t.strip()]
        # optionally enforce tag name validations (e.g. length)
        for name in tag_names:
            if len(name) > 50:
                raise forms.ValidationError(f"Tag '{name}' is too long (max 50).")
        return tag_names

    def save(self, commit=True):
        # Save Post first then process tags
        post = super().save(commit=commit)
        tag_names = self.cleaned_data.get('tags', [])
        # Clear existing tags and add current ones
        post.tags.clear()
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)
        return post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # author and published_date are set automatically
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title", "class": "form-control"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your post...", "class": "form-control", "rows": 8}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Add a comment...",
                "class": "form-control"
            }),
        }
        labels = {
            "content": ""
        }