# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput
from .models import Profile
from .models import Post
from .models import Comment

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
    class Meta:
        model = Profile
        fields = ["bio", "avatar"]

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