\#delete operations in Django



from bookshelf.models import book

book = Book.objects.get(id=1)

book.delete()



\#output

(1, {"bookshelf.Book":1})



\#detailed crud operations



\#command



from bookshelf.models import book

book = Book.objects.get(id=3)

book.delete()



\#output



(1, {"bookshelf.Book":1})



