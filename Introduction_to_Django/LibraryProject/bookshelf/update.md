\#update operations in Django



\#command



from bookshelf.models import book



book = Book.objects.get(id=1)

book.title = "Mastering Django"

book.save()

book.title



\#output



"Mastering Django"

