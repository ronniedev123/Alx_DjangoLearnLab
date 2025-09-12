import os
import django

# Setup Django environment so we can run ORM queries
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library__name=library_name)
print(f"\nLibrarian of {library_name}: {librarian.name}")