# models/user.py

class User:
    """
    Represents a user who can borrow books from the library.
    """
    def __init__(self, name, user_id):
        """
        Initializes a User instance.

        :param name: Full name of the user
        :param user_id: Unique ID for the user
        """
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        """
        Adds a book to the borrowed list.

        :param isbn: ISBN of the book to borrow
        """
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        """
        Removes a book from the borrowed list.

        :param isbn: ISBN of the book to return
        """
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"
