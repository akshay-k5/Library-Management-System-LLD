# Library Management System – Low-Level Design

## Problem Statement
Design and implement a Library Management System that models real-world library operations:
- Add and manage books
- Register and manage members
- Issue a book to a member
- Return a book
- Track book availability (Available / Issued)
- Prevent issuing unavailable books

## High-Level Design
The system follows **Domain-Driven Design** with clear separation of concerns. It is built around three layers:
1. **Models** – Core domain entities: `Book`, `Member`, `BookStatus` enum.
2. **Repositories** – Data access interfaces and in-memory implementations (`BookRepository`, `MemberRepository`).
3. **Services** – `LibraryService` containing all business logic for issuing/returning.

**Dependency Inversion**: The service depends on repository interfaces (abstractions), not concrete implementations. This makes the system easy to extend (e.g., switch to a database).

**Business Rules Enforced**:
- A book can only be issued if its status is `Available`.
- A member cannot issue more than `MAX_BOOKS_ALLOWED` (default 3).
- The same book cannot be issued twice without being returned.
- All operations validate existence of books and members.

## Key Classes and Responsibilities

| Class | Responsibility |
|-------|----------------|
| `Book` | Holds book metadata and status; provides methods to change status safely. |
| `Member` | Stores member info, tracks issued books, enforces max limit. |
| `BookStatus` | Enum for `AVAILABLE` and `ISSUED` states. |
| `BookRepositoryInterface` / `InMemoryBookRepository` | Abstraction and in-memory storage for books. |
| `MemberRepositoryInterface` / `InMemoryMemberRepository` | Abstraction and in-memory storage for members. |
| `LibraryService` | Core orchestrator: add books, register members, issue, return, display catalog/members. |

## OOP & SOLID Principles Applied
- **Single Responsibility**: Each class has one reason to change (e.g., `Book` only handles book state).
- **Open/Closed**: New repository implementations (database, file) can be added without modifying service code.
- **Liskov Substitution**: Repository interfaces allow any implementation to be swapped seamlessly.
- **Interface Segregation**: Repositories expose only necessary methods (add, get_by_id, get_all).
- **Dependency Inversion**: `LibraryService` depends on abstractions, not concrete in-memory stores.

## How to Run
1. Ensure you have **Python 3.7+** installed.
2. Clone the repository:
   ```bash
   git https://github.com/akshay-k5/Library-Management-System-LLD
   cd library-management-system
