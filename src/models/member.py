class Member:
    MAX_BOOKS_ALLOWED = 3  # example limit

    def __init__(self, member_id: str, name: str, email: str):
        self._id = member_id
        self._name = name
        self._email = email
        self._issued_books = []  # list of book_ids

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def issued_books(self) -> list:
        return self._issued_books.copy()

    def can_issue(self) -> bool:
        return len(self._issued_books) < self.MAX_BOOKS_ALLOWED

    def add_issued_book(self, book_id: str):
        if not self.can_issue():
            raise RuntimeError(f"Member '{self._name}' has already issued {self.MAX_BOOKS_ALLOWED} books.")
        if book_id in self._issued_books:
            raise ValueError(f"Book with ID {book_id} already issued to this member.")
        self._issued_books.append(book_id)

    def remove_issued_book(self, book_id: str):
        if book_id not in self._issued_books:
            raise ValueError(f"Book with ID {book_id} was not issued to this member.")
        self._issued_books.remove(book_id)

    def __str__(self):
        return f"Member[id={self._id}, name={self._name}, issued={len(self._issued_books)}]"