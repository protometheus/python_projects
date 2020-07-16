from posts.models import Book


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