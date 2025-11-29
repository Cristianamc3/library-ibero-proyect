# models/book.py

class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, title, author, isbn):
        """
        Initializes a Book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN number (unique identifier)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_loaned = False
        self.is_available = True  # True if the book is available for loan

    def __str__(self):
        return f"{self.title} by {self.author} - ISBN: {self.isbn}"