\#update operations in Django



\#command



from bookshelf.models import book



book = Book.objects.get(id=1)

book.title = "Mastering Django"

book.save()

book.title



\#output



"Mastering Django"



\#detailed crud operations

\#command

from bookshelf.models import Books

book = Book.objects.get(id=3)

book.title = "Nineteen Eighty-Four"

book.save()

book.title



\#output

'Nineteen Eighty-Four'



