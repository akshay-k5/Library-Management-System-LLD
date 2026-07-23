from abc import ABC, abstractmethod
from typing import Optional, List
from ..models.book import Book

class BookRepositoryInterface(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id: str) -> Optional[Book]:
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

class InMemoryBookRepository(BookRepositoryInterface):
    def __init__(self):
        self._books = {}

    def add(self, book: Book) -> None:
        if book.id in self._books:
            raise ValueError(f"Book with ID {book.id} already exists.")
        self._books[book.id] = book

    def get_by_id(self, book_id: str) -> Optional[Book]:
        return self._books.get(book_id)

    def get_all(self) -> List[Book]:
        return list(self._books.values())