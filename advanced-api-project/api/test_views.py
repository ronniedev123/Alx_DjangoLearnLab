from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    """
    Comprehensive tests for CRUD operations,
    filtering, searching, and ordering
    on the Book API endpoints.
    """

    def setUp(self):
        # Create a user for authenticated tests
        self.user = User.objects.create_user(username='tester', password='pass1234')

        # Create authors & books for testing
        self.author1 = Author.objects.create(name='George Orwell')
        self.author2 = Author.objects.create(name='Jane Austen')

        self.book1 = Book.objects.create(
            title='1984', publication_year=1949, author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Animal Farm', publication_year=1945, author=self.author1
        )
        self.book3 = Book.objects.create(
            title='Pride and Prejudice', publication_year=1813, author=self.author2
        )

        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    # ---------------------------
    # Read / List
    # ---------------------------
    def test_list_books(self):
        """List all books (no auth required)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """Retrieve a single book."""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    # ---------------------------
    # Create (requires auth)
    # ---------------------------
    def test_create_book_requires_auth(self):
        """Unauthenticated create should fail."""
        payload = {
            'title': 'Emma',
            'publication_year': 1815,
            'author': self.author2.id
        }
        response = self.client.post(self.create_url, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated create succeeds."""
        self.client.login(username='tester', password='pass1234')
        payload = {
            'title': 'Emma',
            'publication_year': 1815,
            'author': self.author2.id
        }
        response = self.client.post(self.create_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(response.data['title'], 'Emma')

    # ---------------------------
    # Update
    # ---------------------------
    def test_update_book(self):
        """Authenticated update changes book details."""
        self.client.login(username='tester', password='pass1234')
        payload = {
            'title': '1984 - Updated',
            'publication_year': 1950,
            'author': self.author1.id
        }
        response = self.client.put(self.update_url(self.book1.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, '1984 - Updated')

    # ---------------------------
    # Delete
    # ---------------------------
    def test_delete_book(self):
        """Authenticated delete removes a book."""
        self.client.login(username='tester', password='pass1234')
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    # ---------------------------
    # Filtering / Searching / Ordering
    # ---------------------------
    def test_filter_by_publication_year(self):
        response = self.client.get(self.list_url, {'publication_year': 1949})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_by_author_name(self):
        response = self.client.get(self.list_url, {'search': 'Orwell'})
        titles = [b['title'] for b in response.data]
        self.assertIn('1984', titles)
        self.assertIn('Animal Farm', titles)

    def test_ordering_by_title_desc(self):
        response = self.client.get(self.list_url, {'ordering': '-title'})
        titles = [b['title'] for b in response.data]
        self.assertEqual(titles[0], 'Pride and Prejudice')  # should be last alphabetically
