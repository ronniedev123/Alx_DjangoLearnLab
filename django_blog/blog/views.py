from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Post, Comment, Tag
from .forms import CommentForm
from .forms import PostForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile was updated.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})

def home(request):
    return redirect("post-list")  # optional: redirect homepage to posts list

def post_search(request):
    q = request.GET.get('q', '').strip()
    results = Post.objects.none()
    if q:
        # search in title and body; tag names via taggit's tag__name__in or filter via taggit API
        results = Post.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q) |
            Q(tags__name__icontains=q)
        ).distinct()
    return render(request, 'blog/search_results.html', {'query': q, 'results': results})

def posts_by_tag(request, tag_name):
    results = Post.objects.filter(tags__name__iexact=tag_name).distinct()
    return render(request, 'blog/posts_by_tag.html', {'tag': tag_name, 'results': results})

# --- Post CRUD views ---

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # templates/blog/post_list.html
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-published_date"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # templates/blog/post_detail.html
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        # optionally include comments explicitly (Post model related_name is 'comments')
        context["comments"] = self.object.comments.all()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"  # templates/blog/post_form.html

    def form_valid(self, form):
        # set the author to the logged-in user
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def dispatch(self, request, *args, **kwargs):
        # capture post pk from url
        self.post_pk = kwargs.get("post_pk")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # attach author and post
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.post_pk)
        messages.success(self.request, "Your comment was added.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.post_pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Comment updated.")
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})

# Create your views here.
