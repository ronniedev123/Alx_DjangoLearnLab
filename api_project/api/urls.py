from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListAPIView, BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list-create'),
    path('books-list/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]