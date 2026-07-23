from src.models.book import Book
from src.models.member import Member
from src.repositories.book_repository import InMemoryBookRepository
from src.repositories.member_repository import InMemoryMemberRepository
from src.services.library_service import LibraryService

def main():
    # Setup repositories and service (Dependency Injection)
    book_repo = InMemoryBookRepository()
    member_repo = InMemoryMemberRepository()
    library = LibraryService(book_repo, member_repo)

    print("=== Library Management System ===")
    print("Welcome, Librarian!\n")

    while True:
        print("\nChoose an action:")
        print("1. Add a new book")
        print("2. Register a new member")
        print("3. Issue a book to a member")
        print("4. Return a book")
        print("5. Display library catalog")
        print("6. Display all members")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            # Add book
            print("\n--- Add a New Book ---")
            book_id = input("Enter Book ID (string): ").strip()
            title = input("Enter Title (string): ").strip()
            author = input("Enter Author (string): ").strip()
            isbn = input("Enter ISBN (string): ").strip()
            if not book_id or not title or not author or not isbn:
                print("Error: All fields are required.")
                continue
            try:
                new_book = Book(book_id, title, author, isbn)
                library.add_book(new_book)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Register member
            print("\n--- Register a New Member ---")
            member_id = input("Enter Member ID (string): ").strip()
            name = input("Enter Name (string): ").strip()
            email = input("Enter Email (string): ").strip()
            if not member_id or not name or not email:
                print("Error: All fields are required.")
                continue
            try:
                new_member = Member(member_id, name, email)
                library.register_member(new_member)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            # Issue book
            print("\n--- Issue a Book ---")
            member_id = input("Enter Member ID (string): ").strip()
            book_id = input("Enter Book ID (string): ").strip()
            if not member_id or not book_id:
                print("Error: Both Member ID and Book ID are required.")
                continue
            try:
                library.issue_book(member_id, book_id)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            # Return book
            print("\n--- Return a Book ---")
            member_id = input("Enter Member ID (string): ").strip()
            book_id = input("Enter Book ID (string): ").strip()
            if not member_id or not book_id:
                print("Error: Both Member ID and Book ID are required.")
                continue
            try:
                library.return_book(member_id, book_id)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            library.display_catalog()

        elif choice == "6":
            library.display_members()

        elif choice == "7":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()