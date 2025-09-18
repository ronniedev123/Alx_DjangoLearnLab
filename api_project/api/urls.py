from django.urls import path
from .views import BookListAPIView, BookList

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list-create'),
    path('books-list/', BookList.as_view(), name='book-list'),
]