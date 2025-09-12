import os
import sys
import django

BASE_DIR = r"C:\Users\ronal\Alx_DjangoLearnLab\django-models\LibraryProject"
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)

if __name__ == "__main__":
    print("Books by Author 'John Doe':", books_by_author("John Doe"))
    print("Books in Library 'Central Library':", books_in_library("Central Library"))
    print("Librarian for 'Central Library':", librarian_for_library("Central Library"))
