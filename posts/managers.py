from posts.models import Book, Store

# Book service methods
class BookManager:

    @classmethod
    def get_books(cls, incl_publisher=False):
        qs = Book.objects

        # check if prefetch is required
        if incl_publisher:
            qs = qs.select_related('publisher')

        qs = qs.all()
        return qs

    @classmethod
    def get_book(cls, book_id,incl_publisher=False):
        qs = Book.objects

        # check if prefetch is required
        if incl_publisher:
            qs = qs.select_related('publisher')

        qs = qs.get(book_id)
        return qs


# Store service methods
class StoreManager:

    @classmethod
    def store_list(cls):
        qs = Store.objects.prefetch_related('books')

        stores = []

        for store in qs:
            books = [book.name for book in store.books.all()]
            stores.append({'id': store.id, 'name': store.name, 'books': books})

        return stores
