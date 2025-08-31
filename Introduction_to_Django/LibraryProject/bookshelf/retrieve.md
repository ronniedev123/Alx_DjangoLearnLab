\#Retrieve operations in Django



\#command



\#get book id

book = Book.objects.get(id=1)

book.title, book.publication\_year



\#output

("Beginers Django", 2025)



\#detailed crud operations , retrieve

\#command



from bookshelf.models import Book

Book.objects.all()

book = Book.objects.get(id=book.id)

book.id, book.title, book.author, book.publication\_year



\#output

(3, '1984', 'George Orwell', 1949)

