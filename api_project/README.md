\# API Authentication \& Permissions



\## Authentication

This API uses \*\*Token Authentication\*\*:

\- Each user must log in and obtain a token.

\- Include the token in all requests:





\## Endpoints

\- `GET /books/` → List all books (requires authentication)

\- `GET /books/<id>/` → Retrieve a book by ID

\- `POST /books/` → Create a book

\- `PUT /books/<id>/` → Update a book

\- `DELETE /books/<id>/` → Delete a book



\## Permissions

\- By default, only \*\*authenticated users\*\* can access.

\- Can be changed to `IsAdminUser` or custom permissions in `views.py`.



\## Testing

Use Postman or curl:

```bash

curl -X GET http://127.0.0.1:8000/books/ -H "Authorization: Token your\_token"



