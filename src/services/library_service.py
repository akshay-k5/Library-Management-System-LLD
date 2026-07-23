from ..models.book import Book
from ..models.member import Member
from ..repositories.book_repository import BookRepositoryInterface
from ..repositories.member_repository import MemberRepositoryInterface

class LibraryService:
    """
    Core service that coordinates book issuing/returning,
    ensuring business rules are followed.
    """
    def __init__(self, book_repo: BookRepositoryInterface, member_repo: MemberRepositoryInterface):
        self._book_repo = book_repo
        self._member_repo = member_repo

    def add_book(self, book: Book):
        self._book_repo.add(book)
        print(f"Added: {book}")

    def register_member(self, member: Member):
        self._member_repo.add(member)
        print(f"Registered: {member}")

    def issue_book(self, member_id: str, book_id: str):
        member = self._member_repo.get_by_id(member_id)
        if not member:
            raise ValueError(f"Member with ID {member_id} not found.")

        book = self._book_repo.get_by_id(book_id)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")

        # Check if book is available
        if book.status.value != "Available":
            raise ValueError(f"Book '{book.title}' is not available (status: {book.status.value}).")

        if not member.can_issue():
            raise RuntimeError(f"Member '{member.name}' has reached the maximum allowed books.")

        # Update states
        book.mark_issued()
        member.add_issued_book(book_id)
        print(f"Issued '{book.title}' to {member.name}.")

    def return_book(self, member_id: str, book_id: str):
        member = self._member_repo.get_by_id(member_id)
        if not member:
            raise ValueError(f"Member with ID {member_id} not found.")

        book = self._book_repo.get_by_id(book_id)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")

        if book_id not in member.issued_books:
            raise ValueError(f"Book '{book.title}' was not issued to {member.name}.")

        # Update states
        book.mark_available()
        member.remove_issued_book(book_id)
        print(f"Returned '{book.title}' from {member.name}.")

    def display_catalog(self):
        books = self._book_repo.get_all()
        if not books:
            print("No books in library.")
            return
        print("\n--- Library Catalog ---")
        for b in books:
            print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - {b.status.value}")

    def display_members(self):
        members = self._member_repo.get_all()
        if not members:
            print("No members registered.")
            return
        print("\n--- Registered Members ---")
        for m in members:
            books_issued = m.issued_books
            print(f"{m.name} ({m.email}) - Issued books: {books_issued}")