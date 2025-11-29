# main.py

import tkinter as tk
from data_manager import DataManager
from windows.book_registration import RegisterBookWindow
from windows.user_registration import RegisterUserWindow
from windows.loan_return import LoansWindow
from windows.query_view import QueryWindow
from utils.utils import BACKGROUND_COLOR, FONT_TITLE, FONT_NORMAL, BUTTON_COLOR, BUTTON_TEXT_COLOR, PADDING


class LibraryApp(tk.Tk):
    """
    Main window of the library system.
    """

    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("500x350")
        self.configure(bg=BACKGROUND_COLOR)

        # Initialize the data manager
        self.data_manager = DataManager()

        # === Title Label ===
        self.label_title = tk.Label(self, text="Library System", bg=BACKGROUND_COLOR, font=FONT_TITLE)
        self.label_title.pack(pady=15)

        # === Buttons ===
        self.btn_register_book = tk.Button(
            self,
            text="Register Book",
            command=self.open_register_book,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=FONT_NORMAL,
            padx=20,
            pady=5
        )
        self.btn_register_book.pack(pady=PADDING)

        self.btn_register_user = tk.Button(
            self,
            text="Register User",
            command=self.open_register_user,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=FONT_NORMAL,
            padx=20,
            pady=5
        )
        self.btn_register_user.pack(pady=PADDING)

        self.btn_loan = tk.Button(
            self,
            text="Loans & Returns",
            command=self.open_loan,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=FONT_NORMAL,
            padx=20,
            pady=5
        )
        self.btn_loan.pack(pady=PADDING)

        self.btn_query = tk.Button(
            self,
            text="Query Data",
            command=self.open_query,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=FONT_NORMAL,
            padx=20,
            pady=5
        )
        self.btn_query.pack(pady=PADDING)

        self.btn_exit = tk.Button(
            self,
            text="Exit",
            command=self.quit,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            font=FONT_NORMAL,
            padx=20,
            pady=5
        )
        self.btn_exit.pack(pady=PADDING)

    # === Navigation Methods ===

    def open_register_book(self):
        RegisterBookWindow(self, self.data_manager)

    def open_register_user(self):
        RegisterUserWindow(self, self.data_manager)

    def open_loan(self):
        LoansWindow(self, self.data_manager)

    def open_query(self):
        QueryWindow(self, self.data_manager)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
