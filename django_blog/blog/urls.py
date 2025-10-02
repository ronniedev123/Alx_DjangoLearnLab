# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:post_pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("posts/<int:post_pk>/comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("posts/<int:post_pk>/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
