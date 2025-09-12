from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import register_views
from . import views


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path('register/', views.register_view, name='register'),
    path('login/', 
         LoginView.as_view(template_name="relationship_app/login.html"),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name="relationship_app/logout.html"),
         name='logout'),
]
