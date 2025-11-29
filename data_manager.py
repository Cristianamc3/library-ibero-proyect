# gestor_datos.py

from models.book import Book
from models.user import User


class DataManager:
    """
    Manages the data of the library system.
    Stores books and users in memory.
    """

    def __init__(self):
        """
        Initializes the DataManager with empty lists of books and users.
        """
        self.books = []
        self.users = []
        self.loans = []
        self.load_default_books()

    # === BOOK METHODS ===
    def add_book(self, title, author, isbn):
        """
        Adds a new book to the system.
        """
        book = Book(title, author, isbn)
        self.books.append(book)

    def find_book_by_isbn(self, isbn):
        """
        Finds and returns a book by its ISBN.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_all_books(self):
        """
        Returns a list of all books in the system.
        """
        return self.books

    def loan_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_loaned:
                book.is_loaned = True
            return True
        return False
    
    def get_loaned_books(self):
        return [book for book in self.books if book.is_loaned]

    def load_default_books(self):
        self.books.append(Book("Clean Code", "Robert C. Martin" ,"9780132350884"))
        self.books.append(Book("Designing Data-Intensive Applications","Martin Kleppmann" ,"9781491950357"))
        self.books.append(Book("The C Programming Language","Kernighan & Ritchie" ,"9780131103627" ))
        self.books.append(Book("Cien años de soledad","Gabriel García Márquez","9780307474728" ))

    # === USER METHODS ===
    def add_user(self, name, user_id):
        """
        Adds a new user to the system.
        """
        user = User(name, user_id)
        self.users.append(user)

    def find_user_by_id(self, user_id):
        """
        Finds and returns a user by their ID.
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def list_all_users(self):
        """
        Returns a list of all users in the system.
        """
        return self.users

    # === TRANSACTION METHODS ===
    def borrow_book(self, user_id, isbn):
        """
        Allows a user to borrow a book if available.
        """
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_isbn(isbn)
        if user and book and book.available:
            user.borrow_book(book)
            book.available = False
            return True
        return False
    
    def return_book(self, user_id, isbn):
        """
        Allows a user to return a borrowed book.
        """
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_isbn(isbn)
        if user and book and book in user.borrowed_books:
            user.return_book(book)
            book.available = True
            return True
        return False
    