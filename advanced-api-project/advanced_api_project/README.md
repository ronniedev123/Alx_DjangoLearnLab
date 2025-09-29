\## API Views



\### Book Endpoints

\- \*\*List\*\*: `GET /api/books/` – Public

\- \*\*Detail\*\*: `GET /api/books/<id>/` – Public

\- \*\*Create\*\*: `POST /api/books/create/` – Authenticated

\- \*\*Update\*\*: `PUT/PATCH /api/books/<id>/update/` – Authenticated

\- \*\*Delete\*\*: `DELETE /api/books/<id>/delete/` – Authenticated



These views use Django REST Framework generic class-based views for

clean, DRY CRUD operations with custom permission settings.



