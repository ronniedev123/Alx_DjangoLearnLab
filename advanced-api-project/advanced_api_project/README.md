\## API Views



\### Book Endpoints

\- \*\*List\*\*: `GET /api/books/` – Public

\- \*\*Detail\*\*: `GET /api/books/<id>/` – Public

\- \*\*Create\*\*: `POST /api/books/create/` – Authenticated

\- \*\*Update\*\*: `PUT/PATCH /api/books/<id>/update/` – Authenticated

\- \*\*Delete\*\*: `DELETE /api/books/<id>/delete/` – Authenticated



These views use Django REST Framework generic class-based views for

clean, DRY CRUD operations with custom permission settings.



\### Filtering, Searching, and Ordering



Endpoint: `GET /api/books/`



Query Parameters:



| Feature | Param Example | Notes |

|--------|--------------|------|

| Filter | `?title=1984` | Exact match on title |

| Filter | `?author\_\_name=Orwell` | Filter by author name |

| Search | `?search=orwell` | Text search in title and author name |

| Order  | `?ordering=publication\_year` | Ascending year |

| Order  | `?ordering=-title` | Descending title |



Combine multiple:  

`/api/books/?search=animal\&ordering=-publication\_year`



\## Running API Tests



Unit tests are located in `api/test\_views.py`.



Run all API tests:

```bash

python manage.py test api



