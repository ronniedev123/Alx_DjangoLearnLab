\#Create operations in Django



\#command



from bookshelf.models import book

book = Book(title="Beginers Django", publication\_year=2025)

book.save()



\#output



\[<Book: Book object (1)>]>



\#Detailed crud operations



\#command



from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book.save()



\#output

\[<Book: Book object (1)>]>

(Successful)

