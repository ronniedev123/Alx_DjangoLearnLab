from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to everyone (read-only).
    """
    """
    Returns a list of books with filtering, searching, and ordering.

    Query Parameters:
    - Filtering: ?title=1984&publication_year=1949
    - Searching: ?search=orwell
    - Ordering:  ?ordering=title   or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter by exact match on these fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search across these text fields
    search_fields = ['title', 'author__name']

    # Allow ordering by these fields (prefix with '-' for descending)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# DetailView: Retrieve a single book by ID

class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by its primary key (id).
    Accessible to everyone (read-only).
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView: Add a new book

class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Only authenticated users can create.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to add extra logic before saving.
        Example: attach user info or custom logging.
        """
        serializer.save()

# UpdateView: Modify an existing book

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users can update.
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Add custom logic if needed, e.g., track who updated it.
        serializer.save()

# DeleteView: Remove a book

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users can delete.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
