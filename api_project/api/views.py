from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

 """
    API endpoint that allows books to be viewed or edited.

    Authentication:
    - Uses Token Authentication.
    - Each request must include an Authorization header with a valid token:
      Authorization: Token <your_token>

    Permissions:
    - Only authenticated users can access this view.
    - You can customize further using DRF's permission classes
      (e.g., IsAdminUser, custom permissions).
    """

# Create your views here.
