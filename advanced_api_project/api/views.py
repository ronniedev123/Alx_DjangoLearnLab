from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer

# Alternative: Function-based views
@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all().prefetch_related('books')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def author_detail(request, pk):
    author = Author.objects.prefetch_related('books').get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

# Create your views here.
