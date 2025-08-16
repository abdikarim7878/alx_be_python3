# oop/library_system.py

class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)   # call base initializer
        self.file_size = file_size        # in KB

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)   # call base initializer
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition: a Library *has* a collection of books."""
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(book)


__all__ = ["Book", "EBook", "PrintBook", "Library"]
