from .enums import BookStatus

class Book:
    def __init__(self, book_id: str, title: str, author: str, isbn: str):
        self._id = book_id
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = BookStatus.AVAILABLE

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def status(self) -> BookStatus:
        return self._status

    def mark_issued(self):
        if self._status == BookStatus.ISSUED:
            raise ValueError(f"Book '{self._title}' is already issued.")
        self._status = BookStatus.ISSUED

    def mark_available(self):
        if self._status == BookStatus.AVAILABLE:
            raise ValueError(f"Book '{self._title}' is already available.")
        self._status = BookStatus.AVAILABLE

    def __str__(self):
        return f"Book[id={self._id}, title={self._title}, status={self._status.value}]"